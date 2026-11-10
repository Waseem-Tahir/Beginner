# more about dictionries
dic=dict(
    name='waseem',
    age=8,
    fav_tunes='c,d,e'
)
# print(dic)
print(dic.get('name'))   # --> in this type = is to be reminder.
print(dic.get('tunes'))  # --> it give output none.
print(dic.get('names','not found!')) # if the key is not found then you want to see the output not found! on the place of none.

# if in dictionary there are two same variebles then the last one value is consider at the place of that same varieble.
dic2={
    'Name':'waseem',
    'Age':14,
    'Tunes':['l','m','n','o'],   # in this type : is need to be reminder.
    'Age':19
}
print(dic2)      # age in the output is consider 19 in it.
