# find greatest using two func



# def fun1(no1,no2):
#     if no1>no2:
#         return no1
#     return no2
# def fun2(l,no3):
#     if l>no3:
#         return l
#     return no3
# n1=int(input("enter your first no: "))
# n2=int(input("enter your second no: "))
# d=fun1(n1,n2)
# n3=int(input("ener your third no: "))
# f=fun2(d,n3)
# print(f"greatest no is {f}")



# def fun1(no1,no2):
#     if no1>no2:
#         return no1
#     return no2

# def fun2(l,no3):
#     if l>no3:                               # it need to modify later
#         return l
#     return no3
print("       you can splited the no by , only")
n1,n2,n3=input("enter your three no: ").split(",")
n2=int(n2)
n3=int(n3)
n1=int(n1)
# def greatest(n1,n2,n3):
#     # fun1(n1,n2)
#     l=fun1
#     return fun2(l,n3)
# print(greatest(n1,n2,n3))


def fun1(no1,no2):
    if no1>no2:
        return no1
    return no2
def fun2(n1,n2,n3):
    if n1>n2 and n3:                  # now the top one incomplete is now properly complete
        return n1
    elif n2>n1 and n3:
        return n2
    else:
        return n3
def fun3(n1,n2,n3):
    d=fun1(n1,n2)
    return fun1(fun1(n1,n2),n3)
    
print(f"     greator no is   {fun3(n1,n2,n3)}  ")



