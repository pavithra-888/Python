"""a derived class acquires the all the properties of base class"""
print("SINGLE LEVEL".center(50))
class A:
    def a1(self):
        print("this is a1")
class B(A):
    def a2(self):
        print("this is a2")
x=B()
x.a1()
x.a2()
print("MULTILEVEL INHERITENCE".center(50))
class A:
    def a1(self):
        print("this is a1")
class B(A):
    def a2(self):
        print("this is a2")
class C(B):
    def a3(self):
        print("this is a3")
x=C()
x.a1()
x.a2()
x.a3()
print("HIRARICHAL INHERITENCE".center(50))
class A:
    def a1(self):
        print("this is a1")
class B(A):
    def a2(self):
        print("this is a2")
class C(A):
    def a3(self):
        print("this is a3")
x=C()
x.a1()
x.a3()
print("MULTIPLE INHERITENCE".center(50))
class A:
    def a1(self):
        print("this is a1")
class B:
    def a2(self):
        print("this is a2")
class C(B,A):
    def a3(self):
        print("this is a3")
x=C()
x.a1()
x.a2()




