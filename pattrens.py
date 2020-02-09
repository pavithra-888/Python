n=int(input("enter the number"))
for i in range(n):
    print(" "*(n-i)+"* "*(i+1))
n=int(input("enter the number"))
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*(i))
n=int(input("enter the number"))
x=0
for i in range(n):
    for j in range(i):
        print(x,end=" ")
        x=x+1
    print()
n=int(input("enter the number"))
for i in range(n):
    print("* "*(i+1))
n=int(input("enter the number"))
for i in range(n,0,-1):
    print("* "*(i))
