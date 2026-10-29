# while loop is used to run a program multiple times unless the condition will not met.
# i=1
# while i<=10:
#      print(i)
#      i += 1

# i=input("how many no you want to add all of them from 0 to : ")
# i=int(i)
# s=0
# t=0                  # first loop s=1,t=1; second loop s=2,t=3; third loop s=3,t=5 ; forth loop s=4,t=9.
# while s<i:
#     s +=1
#     t =s+1
#     # i +=1
#     # print(f"{j},{}")
#     # print=(f"{s},")
# print(f"total summation of no is {t}")



i=input("enter how many times the no's would you like to sum from 1 to : ")
i=int(i)
k=1
l=0
while k<=i:
                            # for l -> 1,3,6     for k -> 1,2,3
    l=l+k
    k +=1
print(f"the sum of the no's form l to {i} is {l}")

    