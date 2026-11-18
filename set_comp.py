# set comprehesion
# set have no order like 1234...
set_com={p**2 for p in range(1,10)}
print(set_com)

names=['waseem','maisum','sajid']
first_alpha={name[0]  for name in names}
print(first_alpha)           # it output in orderless.
