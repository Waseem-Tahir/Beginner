# dry method
# dry method is used to reduce the progrma size using True,False boolean word.
 
no=int(input("enter a one no b/w 1 to 10: "))
s=5
x=False
while not x: # you don't write False ather not in this loop you must take a varieble to exit the loop after the condtion you met.
    if no == s:   # if you write direct on the place of x then the loop never be stop remember it.
     print("your win the game ")
     x=True
    else:
     no=int(input("enter the no again: "))
