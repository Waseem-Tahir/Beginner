# small exercise called palindrome 
# in this program we reverse the string and to compare it to original string.

string=input("enter the palindrome: ")
# i=0
r=""
for i in range(1,len(string)+1):                   # 1st way of palindrome
    r +=string[-i]
print(r)
if string==r:
    print("string is palindrome")
else:
    print("string is not palindrome")


# String1 = input("enter the palindrome: ")
# r=String1[::-1]
# if String1==r:                                       # 2nd way of palindrome
#     print("string is palindrome")                     
# else:
#     print("string is not palindrome")