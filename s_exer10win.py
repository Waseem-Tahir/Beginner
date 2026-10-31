# small game exercise 
import random
win=random.randint(1,100)
i=0             # varieble i is essential on this time b/s while doesn't declared i at varieble direct like in for loop.
print("hint ( type no is b/w 1 to 100 )")
while i!=win:
  
  i=int(input("enter your winning no: "))
  if i<win:
     print("low no ")
  elif i>win:
     print("enter high no")
  elif i==win:
     print(f"you win {win} is a winning no")
     w=win
     break
     
# i=w
# print(f"now the value of i is : {i}")
    