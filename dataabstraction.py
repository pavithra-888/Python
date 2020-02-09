#data abstraction is nothing but hiding the internal values and shows their functionality
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("i can run and talk")
class Snake(Animal):
    def move(self):
        print("i can crawl")
def main():
    #a=Animal()#When we create the abstract class object it will throw the error because "we can't instantiate abstract class with astractmethod
    x=Human()
    x.move()
    y=Snake()
    y.move()
if __name__=="__main__":
    main()
