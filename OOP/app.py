import csv
import os.path
from dataclasses import dataclass, field
from typing import List, Optional


BOOKS_CSV = "books.csv"
USERS_CSV = 'users.csv'
TRANSACTIONS_CSV = 'transactions.csv'


# TODO: Book data class
@dataclass
class Book:
    book_id: int
    title: str
    author: str
    is_available: bool = field(default=True, init=False, compare=False)


# TODO : Create User class
@dataclass
class User:
    user_id: int
    name: str
    borrowed_books: List[int] = field(default_factory=list, compare=False, init=False)
    LIMIT: int = field(init=False, repr=False, default=float('inf'), compare=False)


# TODO: Teacher data class
@dataclass
class Teacher(User):
    LIMIT: int = 5


# TODO: Student data class
@dataclass
class Student(User):
    LIMIT: int = 3


@dataclass
class Transaction:
    book_id: int
    user_id: int
    action: str # Borrow / return


class FileManager:
    @staticmethod
    def write_csv(file: str, data: List[str]) -> None:
        with open(file,  mode="a", newline="", encoding="utf-8") as f:
            writer_csv = csv.writer(f, delimiter=',')
            writer_csv.writerow(data)

    @staticmethod
    def read_csv(file: str) -> list:
        if os.path.exists(file):
            with open(file,  mode="r", newline="", encoding="utf-8") as f:
                return list(csv.reader(f))
        return []


class BookManager:

    @staticmethod
    def get_books() -> list:
        books = FileManager.read_csv(BOOKS_CSV)
        return books

    @staticmethod
    def __save_books(data: list) -> None:
        FileManager.write_csv(BOOKS_CSV,data)

    @staticmethod
    def add_book(title: str, author: str) -> None:
        books = BookManager.get_books()
        book_id = len(books)+1
        new_book = Book(book_id,title,author)
        BookManager.__save_books([book_id, title, author,])

    @staticmethod
    def search_book(title: str) -> Optional[Book]:
        books = FileManager.read_csv(BOOKS_CSV)
        if found := [b for b in books if b.title.lower() == title.lower()]:
            return found[0]

    @staticmethod
    def remove_book(title: str) -> None:
        book_obj = BookManager.search_book(title)
        if book_obj:
            all_books = BookManager.get_books()
            all_books.remove(book_obj)
            BookManager.__save_books(all_books)


class UserFactory:
    @staticmethod
    def create_user(user_id: int, name: str, role: str) -> User:
        if role == 'Teacher':
            return Teacher(user_id,name)
        return Student(user_id, name)


class UserManager:

    @staticmethod
    def __save_users(users: List[str])->None:
        FileManager.write_csv(USERS_CSV, users)

    @staticmethod
    def register_user(name:str, role: str) -> None:
        users = UserManager.get_all_users()
        user_id = len(users) + 1
        new_one = UserFactory.create_user(user_id, name, role)
        UserManager.__save_users([v for k,v in new_one.__dict__.items()])

    @staticmethod
    def get_all_users() -> list:
        if os.path.exists(USERS_CSV):
            users = FileManager.read_csv(USERS_CSV)
            return [u for u in list(users)]
        return []


class LibraryManager:

    @staticmethod
    def borrow_book(user_id:int, book_id: int ) -> str:
        books: list = BookManager.get_books()
        users: list = UserManager.get_all_users()
        book: Book = next((b for b in books if b.id == book_id), None)
        user: User = next((u for u in users if u.id == user_id), None)

        if not book or not user:
            return 'User or book not found'

        if not book.is_available:
            return 'Book is not available'

        if user.LIMIT <= len(user.borrowed_books):
            return 'You have reach your limit. You not allowed to take an other one.'

        book.is_available = False
        user.borrowed_books.append(book_id)

        LibraryManager.__log_transaction(user_id, book_id)
        return f"{user.name} borrowed book {book.title}"

    @staticmethod
    def __log_transaction(user_id: int, book_id: int, transaction: str) -> None:
        transactions = FileManager.read_csv(TRANSACTIONS_CSV)
        new_transaction = [user_id, book_id, transaction]
        transactions.append(new_transaction)
        LibraryManager.__save_transaction(transactions)

    @staticmethod
    def __save_transaction(data: list) -> None:
        FileManager.write_csv(TRANSACTIONS_CSV, data)


# FileManager.write_csv(TRANSACTIONS_CSV, ['1','1', 'Borrow'])
data = FileManager.read_csv(BOOKS_CSV)
data2 = FileManager.read_csv(USERS_CSV)
data3 = FileManager.read_csv(TRANSACTIONS_CSV)
UserManager.register_user('Petar Popov', 'Student')
UserManager.register_user('Georgi Rashkov', 'Teacher')
print(UserManager.get_all_users())










#
#
#
# # TODO: library data class
# @dataclass
# class Library:
#     lib_id: int
#     address: str
#     available_books: List[Book] = field(default_factory=list, compare=False)
#     customers: List[User] = field(default_factory=list, compare=False)
#
# # TODO: User Manager
# class UserManager:
#
#     @staticmethod
#     def register(usr: User, library: Library) -> None:
#         if usr not in library.customers:
#             library.customers.append(usr)
#             print(f"{usr.name} was registered successfully.")
#             return
#         print(f'{usr.name} already have been registered.')
#
#     @staticmethod
#     def info(usr: str, library: Library):
#         if user_list := [u for u in  library.customers if usr == u.name]:
#             user = user_list[0]
#             print(user)
#             return
#         print(f'{User} not found')
#
#     @staticmethod
#     def borrowing_history(user: User):
#         print('*\n'.join([b.title for b in user.borrowed_books]) if user.borrowed_books else "Empty")
#
#
# # TODO: Books manager
# class BookManager:
#
#     @staticmethod
#     def add_book(book: Book, library: Library):
#         if book not in library.available_books:
#             library.available_books.append(book)
#             print(f'{book.title} was added to the library')
#             return
#         print(f'{book.title} is already in the library')
#
#     @staticmethod
#     def remove_book(book: Book, library: Library):
#         if book in library.available_books:
#             library.available_books.remove(book)
#             print(f'{book.title} was removed to the library')
#             return
#         print(f'{book.title} was not found')
#
#     @staticmethod
#     def search_book(title: str, library: Library):
#         if book_lst := [b for b in library.available_books if b.title == title]:
#             book = book_lst[0]
#             print(f"{book.title} has id: {book.id}")
#             return
#         print(f'The book with title {title} was not found.')
#
#     @staticmethod
#     def list_of_available_books(library: Library):
#         books_titles: list = [b.title for b in library.available_books]
#         print('\n'.join(books_titles))
#
#
# # TODO: RentManager
# class RentManager:
#
#     @staticmethod
#     def borrow_book(book: Book, library: Library, user: User):
#         if book in library.available_books:
#             if book.is_available:
#                 if user in library.customers and user.LIMIT < len(user.borrowed_books):
#                     book.is_available = False
#                     user.borrowed_books.append(book)
#                     print(f'{book.title} have been borrowed by {user.name}')
#                     return
#             return print(f"{book.title} not available.")
#         return print(f"{book.title} not in the library")
#
#     @staticmethod
#     def returned_book(book: Book, library: Library, user: User):
#         if not book.is_available:
#             book.is_available = False
#             user.borrowed_books.append(book)
#             print(f'{book.title} have been returned by {user.name}')
#             return
#
# # TODO: Data manupulation
#
# # TODO:
# # TODO:
# # TODO:
#
# #Book instances
# b1 = Book(1,'Harry Potter', 'JK Rollin')
# b2 = Book(2,'Black Adam', 'Wornner Bros')
# b3 = Book(3,'Spiderman', 'Avenger Troy')
# b4 = Book(4,'The God Father', 'Rocko Balboa')
#
# # User instances
# u1 = User(1,'Georgi Rashkov')
# u2 = Teacher(2,'Petar Petrov')
#
# #library instances
# l = Library(1,'Sofia, st. Don totogo 145', [b1,b2,b3,b4])
#
# #managers
# bm = BookManager()
# um = UserManager()
# um.register(u1, l)
# um.register(usr=u2, library=l)
# rm = RentManager()
# rm.returned_book(b1,l,u1)
# rm.returned_book(b2,l,u1)
# rm.returned_book(b3,l,u1)
# rm.returned_book(b3,l,u1)
# rm.returned_book(b3,l,u1)
# rm.returned_book(b3,l,u1)
# rm.returned_book(b3,l,u1)
# um.borrowing_history(u1)
