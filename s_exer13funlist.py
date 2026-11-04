# exercise for function in list


print("                        Hi how are you what your choice to find sq no.")
print("                    To find sq of no's by range type 1 , by random type 2")
z=int(input("                                   choice no: "))
print("          Rememeber:- The no's don't be seperated by any spaces and another symbol! Thank You.")

if z==1:
    lists=[]
    start_no=int(input("                enter your sq finding start no: "))
    stop_no=int(input("                       enter your sq stop no: "))
    def sq_no(f):
     for i in f:                   # this program take's range value list.
       lists.append(i**2)
     return lists
    d=list(range(start_no,stop_no))
    print(f"                                  {sq_no(d)}")
    
elif z==2:
   list1=input("                   enter the int values in list without seprating the no: ")
   list2=[]
   listf=[]
   def square_no(n):
     for i in list1:
      list2.append(int(i))          # this program take a values in list and outputs it's square.
     for j in list2:
      listf.append(j*j)
     print(f'                                     {listf}')
   square_no(list1)
else:
  print("                                          Sorry...")


























