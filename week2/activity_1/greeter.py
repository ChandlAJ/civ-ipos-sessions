'''Considering reuse (modularisation)
when creating python programs'''
def greet():
    print("Hello, World!")

# create a calculator class and re-use this by instantiating it in the main.py

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b



# So as not to contaminate your global namespace, it is good practice to use a main function.

# so that we can reuse our code as both a module and
# we can use an if statement to ensure that some code is only executed when name is __main__

# module name when imported

    # above is __main__ when running directly
    # only called when a script
