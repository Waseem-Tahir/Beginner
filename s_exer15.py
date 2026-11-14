# exercise that store integer in list using list and type func
# def func(l):
#     p=[]
#     for i in l:
        
#         if type(i)==int():
#             a=str(i)
#             p.append(a)
#         # elif type(i)==list:
#             # for h in i:
#                 # if type(h)==int():
#                 #  g=str(h)
#                 #  p.append(g)
#             # return p
            
#     return p
# r=[]
# s=input("enter the no , str, float any thing seperated by comma : ")
# for j in s:
#     d=str(j)
#     r.append(d)

# liso=[1,2,3,[r],'s','w','i']
# print(func(liso))



def fun_final(l):
    s=[str(i) for i in l if(type(i)==int  or type(i)==float)]
    return s
print(fun_final([1,1.2,'was','mas','adi',[4,3],4,'4',9]))

