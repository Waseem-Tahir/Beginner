# print("hellow world")  # this is my first program that prints 
#                             simple hellow world
# _____________________________________________
                       #    this program print avarage of three no's
# a,b,c=input("enter three no's seperated by ',' to find their avarage : ").split(",") 
# print(f"avarage of the no's is {(int(a)+int(b)+int(c))/3}")
# _______________________________________________
                       #this program change the order of string
# print('Name should be less than 16 character ')
# a = input("Enter your name if you see it to be in reverse order ? ")
# print(a[14::-1])
# _______________________________________________
                # this program take a staring and 
                 # print total length also print one charater len that user input
print("Note that the ',' is must type b/w name and char ")                
a,b =input("Enter your name and the type one char also that you want to see it how many times it come ? ").split(",")

print(f"your name length is {len(a)} and the character length is {a.count(b)}")