# more about sets.
sets={'w',2,5,8,'a','i'}
if 'w' in sets:
 print(" w is present ")
else:
 print(" sorry ")

for items in sets:
 print(items)

s1={1,2,3,4}
s2={2,3,5,6}
print(f"union of set 1 and 2  is {s1|s2}")
print(f"intersection of set 1 and 2 sets is {s1&s2}")