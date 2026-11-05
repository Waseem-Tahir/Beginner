# small exercise that reverse of d list
listd=['ab','bc','ca']
listst1=[]
def rev(l):
        for i in l:
         listst1.append(i[::-1])
        return listst1


# for i in range(0,len(list2d)):
#     # for j in range(0,len(i)):  #  --> it's need to modify later.
#         listst1.append(i)
#         # listst1.reverse()

print(rev(listd))
     
    
