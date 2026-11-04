# more about list

# list1=list(range(1,10))                # method to add data in list.
# print(list1)       

# list2=[1,2,3,'was','mas',2.3,1.1]
# print(list2.index('mas'))              # to find the location in list 

# list3=[1,2,4,2,3,2,0,1,4,6,7,1,7,2,1,6,2]    # indexing method is used to find the location of the data.
# print(list3.index(7,6,))            # 2 is finding no 4 is starting location and 8 is stoping location point.
# print(list3.index(6,4))         # --> in this type it print the first loction from left to right and print 9 location,

# print(list3.pop())         # it will delete the last element of the list data.
# list4=list2.pop()        # it strore the delete data from the list.    
# print(list4)        


# list0=[1,2,3,4,5,6,7,8,9]
# listnev=[]
# for i in list0:
#     listnev.append(-i)          # in this short program it will change the no in -no's.
# print(listnev)


# liste=['a','b','c','d','e']     # why this line is wrong i need to be know it later.
liste=[1,2,3,4,5]
listadd=[]
def fun_list(l):
    
    for i in l:
     listadd.append(-i)
    return listadd
print(fun_list(liste))
    
    




