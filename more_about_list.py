# more about list
# insert method
# append method
# add method

list1=[1,2,3,4]
list1.insert(1,3)   # -->   # it insert 3 after 2 not on the place of 2
print(list1)

list2=[1,2,3]
list3=[4,5,6]           
list4=list1+list2   # -->    # this method is only suitable if the data is string type e.g below 1.1
print(list4)


lis1=['apple']
lis2=['orange']
lis3=lis1+lis2      # -->     # example 1.1
print(lis3)

lis4=["pear"]
lis5=["kivi"]
lis5.append(lis4)   # -->     # in this type it print list inside list
print(lis5)

L1=['kivi']
L2=['mango']
L2.extend(L1)      # -->  # in extend method list inside list is not print like append method
print(L2)          