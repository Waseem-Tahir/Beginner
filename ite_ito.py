# iterator and iterables
# an iterable is an object that allows you to access its elements one by one, 
listA=[1,2,3,4,5]    # it is iterables     # while an iterator is an object that 
listB=map(lambda q:q,listA)    # --- it is iterator   # produce values at one at a time when you call it next() method.

# example 1
# print(next(listA))  # it generates error because it is not an iterator.

                      # example of iterables is list,tuple,dict,set,and string.

# example 2
print(next(listB))   # it generates correct answer because it's an iterable.
print(next(listB))
print(next(listB))

# example 3
listnew=iter(listA)
print (next(listnew))
print (next(listnew))
print (next(listnew))
print (next(listnew))
print (next(listnew))
