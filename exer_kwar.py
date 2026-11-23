# exercise of kwards
# def capi(l):
#     m=[]
#     for p in l:
#         m.append(p.title())
#         return m
# print(capi['waseem','maisum','adil'])

# def capi(l):
    # m=[]
    # for p in l:
        # s=p.title()
        # m.append(s)
    # return m
# print(capi['waseem','maisum','adil'])


o=0
def capi(l,**kwargs):
    if kwargs.get("reverse"):           # .get() holds the key value of the dictionary
        return[j[::-1].title() for j in names]
    else:
        return[j[::1].title() for j in names]
names=['maisum','waseem','adil']
s=capi(names)
r=capi(o,reverse=True)          # ensure that argument key should not be in '' string format.
print(s)
print(r)
