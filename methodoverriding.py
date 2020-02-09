class A:
    def addition(self):
        print("this is first addition")
    def substraction(self):
        print("this is sub substraction")
class B(A):
    def addition(self):
        super().addition()
        print("this is second addition")
x=B()
x.addition()
"""we have two classes with two methods with same name  and same parameters"""