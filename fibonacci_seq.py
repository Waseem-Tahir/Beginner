# fibonacci sequences
a=0
b=1
n=int(input("enter the fibonacci no: "))
if n==1:
    print(a)
elif n==2:
    print(a, b)
else:
    print(a,b,end=" ")             # this program is small difficult intesresting but still incomplete.
    for i in range(1,n-2):
        c=a+b     # 1,2,3,5        # i think in b or c or another varieble it comes in order of this 1,2,3,4,5,6 and so on...
        a=b       # 1,1,2,3
        b=c       # 1,2,3,5
        # print(b,end=" ")
        print(c,end=" ")


