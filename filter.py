# filter odd and even no in the list 
print ("   please take space b/w the no's")
a=input("enter the no's you want to filter: ")
a=a.split()
# print(type(a))
b=[]
e=[]
o=[]
lf=[o,e]
def even_odd(r):
    for i in a:   # once i in a means it take a location no second i in range mean(1,len(a)) mean it fixed the value from 
     e=int(i)                                                                                           # 1 to length of a.
     b.append(e)
    return b
# b=b
# print(b)
# print(len(b))
b=even_odd(a)
for i in b:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(lf)

    