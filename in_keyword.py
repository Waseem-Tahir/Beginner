# in keyword in python 
# in keyword word is used to check the special or particular character is presence in the string or not
city="Lahore"
city=city.lower()
type_character=input("enter the check character: ")
type_character=type_character.lower()
if type_character in city:
    print("type character is presence")
else:
    print("sorry your type character is not found in the string.")