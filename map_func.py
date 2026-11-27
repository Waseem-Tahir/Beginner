# map function
# map() function applies a given function to all items in an iterable 
# (like a list) and returns a map object (which is an iterator). You can 
# convert the map object to a list or other iterable types.


# for example
numbers = [1, 2, 3, 4, 5]
lis=[x**2 for x in numbers]
print(lis)

# now in map function
sqno=map(lambda c:c**2 ,numbers)
print(sqno)  # this will print the map object, not the list of squared numbers
sqno=list(sqno)  
print(sqno)

