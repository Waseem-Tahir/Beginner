# intro of *args 

# arg with parameters
def s(a,b):
    sum=a+b
    return sum
def args(*arg):
    sums=0
    print(arg)
    print(type(arg))
    for d in arg:
        sums +=d
    return sums   
print(s(2,3))
f=args(3,4,5,3)
print(f)

# arg with arguments

def argu(*ag):
    multiply=1
    for w in ag:
     multiply *=w
    return multiply
r=[1,3,7]
print(argu(*r)) 







