# list comprehension with if else function
# o=[]
def func(f):
    o=[2*r if (r%2==0) else -r for r in f ]
    return o
print(func([1,2,3,4,5,6,7,8]))


# mixed =[r*2 if (r%2==0) else -r for r in f]