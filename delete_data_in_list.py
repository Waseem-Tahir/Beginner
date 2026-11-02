# delete data from list

list1=[1,2,3,4,5]
list1.pop()      # in this line the end data is delete only.
print(list1)     # pop method is used to delete data from list it delete the last data from the list.
list1.pop(2)     # in this line it delete the data presence in the place of 2. 
print(list1)
                                                               # --> to insert data (insert,extend,append).
                                                               # --> to delete data     (del,pop,remove).
list2=[1,2,3,4,5]
print(list2.pop())                    # -->       # in this line it print the pop data .
print(list2)

list3=['was','mas','irf','vir','mus','moh','jav']
list3.clear()       # -->           # clear delete all data in the list if you put the address of no in th (3) it give error.
print(list3)
list4=['was','mas','irf','vir','mus','moh','jav']
list4.remove('vir')                    # -->      # remove method is used to remove the special data from the list.
print(list4)

list5=['was','mas','irf','vir','mus','moh','jav']
del (list5[5])  # -->   # it delete the data if the address is given it need to be pass address of delete data else give error.
print(list5)