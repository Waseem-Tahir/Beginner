# small exercise of function that find take two no and find which is greater
def greater(no1,no2):  # the funtion parahesis is called paramenter
    if no1<no2:
        print(f"sec no {no2} is greater then {no1}")
    else:
        print(f"fir no {no1} is greater then {no2}")
n1=int(input("enter your first no: "))
n2=int(input("enter your second no: "))
d=greater(n1,n2)  # the calling parathesis is are argument 
