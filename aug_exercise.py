# exercise using aug

# def argu(n,*aug):
#     b=[]
#     b=[n**w for w in aug  ]
#     return b
# # listp=input("enter the no's list")              # my mistakes
# s=[1,2,3,4,5,6]

# exp_no=int(input("enter the exponent no : "))
# out=argu(exp_no,s)


def argument(n,*argu):
    if argument:
        return[ s**n for s in argu]
    else:
        print("sorry you not passed any argument")
expo=input("enter you exponent no: ")  
expo=int(expo)
lis=input("eneter your list ")  
m=[]
for r in lis:
    q=r
    q=int(r)
    m.append(q)

print(argument(expo,*m))