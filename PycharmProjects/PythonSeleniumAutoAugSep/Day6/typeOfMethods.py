"""

https://realpython.com/instance-class-and-static-methods-demystified/

https://docs.python.org/3/tutorial/classes.html

"""

class TypeOfMethods():

    def __init__(self):
        print("I am special method..")


    def instanceMethod(self):
        print("Instance method...")


    @classmethod
    def classMethodDemo(cls):
        print("class method...")


    @staticmethod
    def staticMethod():
        print("static method...")

# object of the class

t = TypeOfMethods()

t.instanceMethod()
t.classMethodDemo()
t.staticMethod()
TypeOfMethods.classMethodDemo()
TypeOfMethods.staticMethod()