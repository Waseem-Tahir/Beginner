# reversing list using list comprehension and function.

# def rev(l):
#     r=[]
#     for n in l:
#           r.append(n[::-1])
#     return r
# print(rev(['was','adi']))

def rev(l):
    return[s[::-1] for s in l]
print(rev(['irf','adi','maj']))

    



        
