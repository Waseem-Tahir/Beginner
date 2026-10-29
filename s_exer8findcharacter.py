# small exercise that take string and count which character is how many times in that string
string=input("enter your string: ")
i=0
b=0
tem_var=""
while i<len(string):
 
 if string[i] not in tem_var:
       tem_var +=string[i]
       b=string.count(string[i])
       print(f"{string[i]} is {b} times")
 i +=1


