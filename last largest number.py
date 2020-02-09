x=[23,2,34,2,4,3,333,90,839]
for i in range(len(x)):
    for j in range(i,len(x)):
        if x[i]<x[j]:
            x[i],x[j]=x[j],x[i]
print(x[1])