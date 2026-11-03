# list inside list 

list1=[[1,2,3],['was','mas','adi'],[2,4,6]]   # list inside list two list called 2D list.
#  list 2[[[2,5],[1,3]],[[2,2],[1,3]]]        # this type of list is called 3D list.
for dual in list1:
    for inside in dual:
        print(inside)


print(list1[1][1])  # --> output is mas             # for access in the list 