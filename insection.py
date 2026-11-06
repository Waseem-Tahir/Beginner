# to find intersection of two list.
list1=input("enter your list one: ")
list2=input("enter you list two: ")
list1=list1.split()
list2=list2.split()
lis1=[]
lis2=[]
f=[]
for i in list1:
     a=int(i)
     lis1.append(a)
  
z=[]
for j in list2:
     b=int(j)
     lis2.append(b)
for k in lis1:
    if k not in z: 
          if k in lis2:
               r=k
               f.append(r)  
               z.append(r)
                    
print(f)    
# print(lis1)
# print(lis2)



