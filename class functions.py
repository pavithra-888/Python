class Employee:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
x=Employee("raju",100,24)
print(getattr(x,'name'))#get the attribute of the object.
setattr(x,'age',34)#set the perticular attribute of the object.
print(getattr(x,'age'))
#delattr(x,'id')#delete the pericular attribute of the object.
print(getattr(x,'id'))
print(hasattr(x,'ide'))#it returns the true if object contain the attribute