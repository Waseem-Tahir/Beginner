# dictionary comprehension
# square of the no's

dic_com={no:no**2 for no in range(1,11)}

for x,y in dic_com.items():
    print(f"the no is {x} and its square is {y}")

stri="Skarduu"
dic={no:stri.count(no) for no in stri}
print(dic)