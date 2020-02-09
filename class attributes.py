class Employee:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def display(self):
        print("my name is {}\n.and age is {}\nand my id is {}"%(self.name,self.age,self.id))
x=Employee('raju',300,23)
print(x.__dict__)
print(x.__doc__)
#__x.__module__
# x.__name__ it is used to access the class name
print(x.__module__)
#print(x.__name__)
#print(x.__bases__)