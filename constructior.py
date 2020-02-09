""" constructor is a reserved method and it is used to intialize the instance members of the class
   when we create the object of this class that time consturctor is executed autometically
   1.parameterized constructor
   2.non-parameterized constructor"""
#1.Non-parameterized constructor
class Student:
    def __init__(self):
        print("this is the Non-parametrized constructor")
    def show(self,name):
        print("hello",name)
x=Student()
x.show('raju')
#parameterized constructor
class Employee:
    def __init__(self,name):
        print("this is the parameterized constructor")
        self.name=name
    def show(self):
        print("hello",self.name)
y=Employee("Jhon")
y.show()
