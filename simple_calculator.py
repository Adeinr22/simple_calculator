from tkinter import *

class Calculator():
    def __init__(self):
        pass

    def addition(self):
        pass

    def substraction(self):
        pass

    def multiplication(self):
        pass

    def division(self):
        pass

    def clear(self):
        pass

    def result(self):
        pass

class App(Tk, Calculator):
    """handles window initialization"""
    def __init__(self, title="Simple Calculator 5000", geometry="400x600"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(False, False)

    def typing(self):
        pass

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    calculator = App()
    calculator.run()