# update in dictionary
d=dict(
    Name='maisum',
    Class='8',
    Age=15,
    Skills=['hard working','smart working','deep thinker']
)
print(d)
print(type(d))
l={'Class':12,'Age':18}
d.update(l)  # --> this is the clear method to update our dictionary.
print(d)
popped=d.pop('Skills')
print(type(popped))