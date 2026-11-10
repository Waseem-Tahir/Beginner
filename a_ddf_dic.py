# add and delete data from dictionaries
dic={
    'name':'Maisum',
    'class':8,
    'age': 15,
    'hobbies':['stdying','cricket']

    
}
dic['fav  tunes']=['a','b','c','d'] # --> this way is used to add data in dictionaries.
print(dic)
popped_item=dic.pop('hobbies')   # --> this way is used to delete data from dictionaries.
print(popped_item)
print(type(popped_item))
popped_item2=dic.pop('age')
print(popped_item2)
print(type(popped_item2))
dic['studying colleges']=['pcs','cds']
print(dic)


