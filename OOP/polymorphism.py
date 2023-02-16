"""
Polymorphism is ability of objects of different classes to be treated as objects of the same class.
"""


# TODO Polymorphism


class Pycharm:
    def compile(self):
        print('Pycharm compiling.,. ')


class VSCode:
    def compile(self):
        print('VSCode compiling.,. ')


class Laptop:

    def __init__(self, ide):
        self.ide = ide

    def load_file(self):
        self.ide.compile()


vs = VSCode()
py = Pycharm()
program = Laptop(py)
program.load_file()
