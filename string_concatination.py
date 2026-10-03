# string concatinaton
data=input("enter a data : ")
print("gilgit " + data)   # the input data is always declared by string in python.
# print(4+data)             # it give error because in python you don't add string with integer you need to convert data into int.
print(str(4) + data)      # it give correct answer if the input data is whatever because input data declared string in python and given 4 is also is in string format.
print(int(data)+4)        # it also give correct answer if the data is whatever because in this we can see data is converted in int format.
