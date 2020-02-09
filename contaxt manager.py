"""Context managers are a way of allocating and releasing some sort of resource using with keyword
when i use with keyword in file handling it will autometically close the files"""
f=open("raju.txt",'w')
try:
    f.write("banglore is metro city")
finally:
    f.close()
from contextlib import contextmanager
@contextmanager
def manged_file(name):
    try:
        f=open(name,'w')
        yield f
    finally:
        f.close()

