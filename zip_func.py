# zip funcion
# zip funtion is used to zip two differnt list or more thaen two list in one list or tuple.
list1=['user1','user2','user3']
list2=['waseem','maisum','janghi']
list3=['apple','mango','banana']
listzl=list(zip(list1,list2))
listzd=dict(zip(list1,list2))
listzt=tuple(zip(list1,list2,list3))
# listzd2=dict(zip(list1,list2,list3)) # --> it is wrong generate error because for dict max include two list for zip only.
print(listzl)
print(listzd)
print(listzt)



# example 2
listfi=[]
lista=[1,4,3,6]
listb=[2,3,5,1]
# listzi=tuple(zip(lista,listb))
# listf.append(list(zip(max(lista,listb))))
listf=[listfi.append(max(pair)) for pair in zip(lista,listb)]     # an interesting line.
print(listfi)


