import copy
print("this is shallow copy")
a=[[1,2],3,4,5,6]
b=copy.copy(a)  #this is copy object of a
b[0][1]=234     #i want to change the copy object value it will reflect original object also
print(b)
print(a)
print("this is deep copy")
#above problem overcome by the deep copy
c=[[1,2],3,4,5,6]
d=copy.deepcopy(c)
d[0][1]=234
print(d)
print(c)

