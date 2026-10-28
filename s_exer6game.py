# small game exercise 2
# in this game if the user name begin with letter a and his age abouve 10 then he see the game other wise he doesn't.
user_name,age=input("enter your name: \nyour age: ").split(",")
age=int(age)
user_name1=user_name[0]
user_name2=user_name1.lower()
if user_name2=="a" and age==10:
    print("you can play this game")
elif user_name1==user_name2 or age!=10: 
    print("sorry you are not play this game \n your age issue")
elif user_name1!=user_name2 or age==10:
    print("sorry you are not play this game \n you name first letter is not start with a letter")
elif user_name1!=user_name2 and age!=10:
    print("your age and name first letter both are issue \n you are not play this game")

                    
