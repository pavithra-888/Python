class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return "the total pages"+str(self.pages)
x=Book(100)
print(x)