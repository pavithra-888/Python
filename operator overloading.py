"""we have to add two objects with binary ‘+’ operator it throws an error, because compiler don’t know how to add two objects.
So we define a method for an operator and that process is called operator overloading"""
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
x=Book(100)
y=Book(200)
print(x+y)