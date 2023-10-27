import random

#variable assignment
win, loss = 0, 0
lineb, tabs, hyphen = "=", "\t", "-"
Exit = True

#functions
def welcome():
    username = input("Enter your name please:\n-> ")
    print(f"{lineb * 50}\nHello {username} and Welcome to Rock/Paper/Scissors Game\n{lineb * 50}\n")
    return username
username = welcome()
def play(user,computer,win,loss):
    if (user == "scissors" and computer == "rock") or (user == "paper" and computer == "scissors") or (user == "rock" and computer == "paper"):
        loss += 1
        result = "loss"
    else:
        win += 1
        result = "win"
    print(f"\n{username} choice :\n->{user}\nComputer's choice :\n->{computer}\n\nso it's a {result}\n")
    if result == "win":
        print(f"{user} beats {computer}\n")
    else:
        print(f"{computer} beats {user}\n")
    return win, loss
def userchoice():
    while True:
        user = input("What's your choice? (\"rock\", \"paper\" or \"scissors\")\n-> ").lower()
        if user not in choices:
            print("#Error! Please enter a valid choice.#")
        else:
            return user
def again():
    while True:
        replay = input("Do you want to continue? Yes / No\n-> ")
        if replay.lower() == "yes":
            return True
        elif replay.lower() == "no":
            print(f"{hyphen * 40}\nscore\n{hyphen * 40}\n- {username} -\nwins -> {win}\nloss -> {loss}\n{lineb * 40}\n"
                  f"- Computer -\nwins -> {loss}\nloss -> {win}\n{hyphen * 40}\n{tabs * 4}Byebye!", end=f"\n{hyphen * 40}")
            return False
        else:
            print("please choose Yes or No.")

while Exit:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    user = userchoice()
    if user == computer:
        print("it's a tie, do over")
        continue
    win,loss = play(user,computer,win,loss)
    Exit = again()