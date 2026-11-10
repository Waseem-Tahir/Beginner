# fromkeys and gets method in python.
# fromkey is used to create the keys and store the same vlues in all the key .
# in this programing we talk about four methods formkey,get,copy and clear mehtod.

d=dict.fromkeys(['sub1','sub2','sub3','sub4'],'unknown') # --> in this way formkeys is to be declare.
d2=dict.fromkeys(['isl','pst'],['unknown,unknown'])
d3={
    'name':'waseem',
    'age':20,
    'games':['snoker','riding','swimming']

}
dicfr=dict.fromkeys ((range(1,10)),'unkonw') # 2nd mehod of using formkeys using range fun().
print(dicfr)

print(d)
print(d2)
popped_items=d3.popitem() # --> pop item is delete the end value.
print(d3)
print(d3)
print(popped_items)

print(d2.get('pst'))  # in this line of code pst value is detected using .get() method

if d3.get('age'):
  print("yes")
else:
  print("no")

dc=d2.copy()  # --> copy method.
if dc==d2:    # --> check weather dc items == d2 items?
  print("ok")
else:
   print("no")

if dc is d2: # --> check is both variebles show the same locations?
  print("yes")
else:
  print("no")