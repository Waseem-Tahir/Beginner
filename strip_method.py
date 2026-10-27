# strip method 
# strip method is used to remove space in the word before or after or both

# name,character=input("enter the name and count charcater : ").split(",")
# print(f"length of name is {len(name)} length of character is {name.strip().lower().count(character.strip().lower())}")

name="     hellow      "
print(name.lstrip())
print(name.rstrip())
print(name.strip())

print(name.replace(" ","")+"...")