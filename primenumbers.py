start=int(input())
end=int(input())
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
print("check the given prime number of not")
n=int(input())
for i in range(2,i):
    if n%i==0:
        print('this is not prime number')
        break
else:
    print("this is prime number")
