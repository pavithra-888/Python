class Student:
    counter=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.counter=Student.counter+1
    def msg(self):
        print(self.name,"\t",self.marks)
    @classmethod
    def raju(cls):
        return cls.counter
    @staticmethod
    def rajesh(age):
        if age<17:
            print("school")
        else:
            print("college")
a=Student('raju','95')
b=Student('rajesh','89')
a.msg()
print(a.raju())
Student.rajesh(34)