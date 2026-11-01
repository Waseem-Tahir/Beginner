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



def fun1(no1,no2):
    if no1>no2:
        return no1
    return no2
def fun2(l,no3):
    if l>no3:
        return l
    return no3
n1=int(input("enter your first no: "))
n2=int(input("enter your second no: "))
n3=int(input("ener your third no: "))
def greatest(n1,n2,n3):
    fun1(n1,n2)
    s=fun1
    return fun2(s,n3)
print(greatest)
