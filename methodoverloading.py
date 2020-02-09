def product(a,b):
    return a+b
def product(a,b,c):
    return a+b+c
print(product(1,2,5))
"""if we have one class with two methods and same name but different arguments
   python doesn't support the method overloading"""
class A:
    def product(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
x=A()
print(x.product(1,2,4))


