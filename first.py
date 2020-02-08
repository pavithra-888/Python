str="aaaabbbccd"
from collections import Counter
x=dict(Counter(str))
a=[i for i in x.keys()]
b=[i for i in x.values()]
c={i:j for i,j in zip(b,a)}
print("the maximum occurence in string  ",c[b[0]])
print("the second occurence in string  ",c[b[1]])
print("the maximum occurence in string  ",c[b[2]])
