# more about dictonary
dic={
    'name':'waseem',
    'age':24,
    'games':['hockey','cricket','vollyball']
}
if 'name' in dic:  # --> this type is used for key values.
  print("ok")
else:
 print("no")

if 'waseem' in dic.values():  # --> this type is used to fetch dictionary values.
  print("yes")
else:
  print("no")

if 'name' in dic.values(): # --> .values() func is used to check out the values in the dictionary.
  print("ok")
else:
  print("no")


for i in dic.values():   # to detect speical values in the dictionary
  print(i)

for i in dic:
  print(i)

dis=dic
print(dis)
print(type(dis))
print(dis)

dic2=dic.values()   
print(type(dic2))   # it consider at a list but it is not list need to rememeber.

for i,j in dic.items():  # .items() fun is used to store the values in key is sequence wise.
  print(f"key is {i} values is {j}")

for i in dic.items():
  print(i)
  