import random

def generatenum():
    while True:
        number = random.sample(range(10), 4)
        if number[0] != 0:
            return ''.join(map(str, number))
def check(n,guess):
    guess = str(guess)
    bull,cow = 0,0
    for index,i in enumerate(str(n)):
        if i in guess:
            if guess.index(i) == index:
                bull += 1
            else:
                cow += 1
    return bull, cow
def user():
    while True:
        user = input("enter your 4 digit guess:\n-> ")
        if not user.isnumeric() or len(str(user)) != 4 or len(set(user)) != len(str(user)):
            print("#Error!")
            continue
        else:
            return user
def again():
    while True:
        read = input("play again?\n-> ").lower()
        if read != "no" and read != "yes":
            print("#Error!, (Yes/No)")
            continue
        elif read == "yes":
            return True
        return False
def tries():
    while True:
        read = input("enter number of tries\n-> ")
        if not read.isnumeric():
            print("please enter valid number!")
            continue
        elif int(read) > 40:
            print("max is = 40")
            continue
        return int(read)
win = False
while True:
    cmp = generatenum()
    count = tries()
    print(cmp)
    while count > 0:
        number = user()
        bull, cow = check(number,cmp)
        if bull == 4:
            print("right guess!")
            win = True
            count = 0
            continue
        else:
            print(f"{number}\nbull -> {bull}\ncow -> {cow}")
        count -= 1
    else:
        if not win:
            print(f"number of tries are done\nthe right answer is :{cmp}")
        if again():
            continue
        else:
            print("bye bye!")
            break
