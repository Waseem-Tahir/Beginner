# filter function 
# fitler funciton is used on that time when you need to store the specific items in the list only.
# one thing need to be remember that map() and filter() both iterates one time only.

# for exemple in for loop
listw=[]
lista=[1,2,3,4,5]
for p in lista:
    if p %2==0:
     listw.append(p)
print(listw)

# for exemple in list comprehension
listq=[1,2,3,4,5,6]
listc=[o for o in listq if o%2==0]
print(listc)

# now in filter func
liste=[1,2,3,4,5,6,7]
l=tuple(filter(lambda x:x%2!=0,liste))     # use lambda for easy to use in map and filter function.
print(l)
