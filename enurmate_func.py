# enurmate function
# enurmate function is used to iterate over a list and get the index of the element 
#   along with the element itself. It returns a tuple containing the index and the element.

names = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(names):    # i takes the location while name takes the value of that location.
    print(f"Index: {i}, Name: {name}")

def enumerate_example(lst2,lst):
    # # return [a for a in lst2 if a in enumerate lst2 else print(-1)]
    for a,c in enumerate(lst2):
        if c == lst:
            return a
        return -1
# print(enumerate_example('adi',['mas','was','adi'])) # --> it is wrong because the first argument
print(enumerate_example(['mas','was','adi'],'mas'))           # should be a list, not a string. The correct call would be: