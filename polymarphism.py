class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")
class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")
def flying_test(bird):
    bird.fly()
x=Parrot()
y=Penguin()
flying_test(x)
flying_test(y)
"""the above program we defined two classes Parrot and Penguin. two classes of have common methods.but their fuctions are different
   to allow polymarphism, we create common interface function that can take any object. then we passed the x and y in function,it can run effectively """
