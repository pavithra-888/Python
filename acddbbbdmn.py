import re
n = input()
y = []
for i in n:
    i = i * 3
    if re.search(i, n):
        x = n.split(i)
        n = "".join(x)
        y.append(n)
    else:
        pass
print(y[-1])
print(len(y[-1]))
