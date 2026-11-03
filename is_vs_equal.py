# is vs equal
num=['mango','apple','banana','orange']
num2=['kivi,berry,stabary,lemon']
num3=['mango','apple','banana','orange']
num4=['mango','apple','berry','lemon']
num5=num

if num is num3:
    print("both are equal")
else: 
    print("both are not equal")

if num==num3:                  # equal always chek is the list1 and list2 are both data present them are equal or not.
    print("both are equal")
else:
    print("both are not equal")

if num is num5:                 # is always check is the list represent the same varieble store in memory.
    print("both list are equal")
else:
    print("both are not equal")