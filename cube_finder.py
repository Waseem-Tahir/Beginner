# cube finder using dictionary
d=dict()
c=0
def cubefin(n):
    for i in range(1,n):
      c=i*i*i 
      d[i]=c
    return d
print(cubefin(4))
