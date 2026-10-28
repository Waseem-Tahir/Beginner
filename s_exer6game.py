# small game exercise 2
# in this game if the user name begin with letter a and his age abouve 10 then he see the game other wise he doesn't.
user_name,age=input("enter your name: \nyour age: ").split(",")
age=int(age)
user_name1=user_name[0]
user_name1=user_name1.lower()
if user_name1=="a" and age==10:
    print("you can play this game")
else:
    print("sorry you are not play this game")


                    
