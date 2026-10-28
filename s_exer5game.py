# small game exercise
user_input=input("enter one random no b/w 1 to 10 to win the game: ")
# user_input1=0
random_no=6
if user_input==6:
    print("Congratulations\nyou win the game")
    break()
else:
    user_input1=input("try once chance more ")
    if user_input1==6:
        print("Congratulations\nyou win the game")
    elif user_input1>6:
        print("you type a highest no")
    else:
        print("you type a lowest no")