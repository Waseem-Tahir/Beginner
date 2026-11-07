# how to insert list inside list
lists=input("                 enter the first list: ")
lists=lists.split()
list=[]
for i in lists:
  a=int(i)
  list.append(a)
# print(list)



print("      enter 1 if you want to add list enter 0 if you want stop entry list.")
for j in range(1,10000000000):
    
    
    b=int(input("                      1 or 0 : " ))
    if b==1:
       c=input("         input the list inside list: ")
       c=c.split()
       lists.append(c)
    elif b==0:
       break
print(lists)




# list=[1,2,3,4]
# list2=[6,8,6,5]
# lists=[]
# list.append(list2)
# print(list)


    

