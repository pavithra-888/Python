"""encapsulation is nothing to restric to access the methods and variables and the prvent dataf from direct modification if nothing but encapsulation"""
class A:
    #def __init__(self):
        #self.__update()
    def driving(self):
        print("this is driving")
    def __update(self):
        print("the software update")
x=A()
x.driving()
#x.__update()#we can't access the private method outside of the class