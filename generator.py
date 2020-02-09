#generators are used to creating the iterators with the different approches
from time import sleep
n=int(input("enter the number"))
print("contdown start")
def countdown(n):
    while n>0:
        yield n
        n=n-1
        sleep(0.3)
x=countdown(n)
for i in x:
    print(i)