# small exercise using for loop


# l=int(input("enter the no that you want to add from 1 to that is: "))
# # i=1
# k=0
# # j=1
# for j in range (l+1):
#      print(f"the loop checking : {j}")
#      k +=j
# print(f"the sum of all the no from 1 to your choice no is {k}")



# small another exercise using for loop to sum the user input no like 123432 etc.

# q=input("enter the no that you want to add them: ")
# w=0

# for e in range(len(q)):
#     r=int(q[e])
#     w +=r
# print(f"the summation of the no is {w}")

 # small further exercise of for loop to find the len of string and to find the char how mush is it in the string.

p=input("enter the string : ")
temp_var=""
p=p.lower()
for i in range(len(p)):

    if p[i] not in temp_var:
      temp_var +=p[i]
    #   o=p.count(p[i])
      print(f"the char is ' {p[i]} ' it is ' {p.count(p[i])} ' times is in the string.")               
    #   temp_var +=p[i]
    

     
