import random

easy1 = random.randint(1,10)
easy2 = random.randint(1,10)
normal1 = random.randint(11,111)
normal2 = random.randint(11,111)
hard1 = round(random.uniform(1, 100),1)
hard2 = round(random.uniform(1, 100),1)
def addition():
    difficulty = input("Select between Easy,Normal or Hard")
    if difficulty == "Easy":
        easyAddition()
    elif difficulty == "Normal":
        normalAddition()
    elif difficulty == "Hard":
        hardAddition()
def easyAddition():
    answer = int(input(f"What is {easy1} + {easy2}?"))
    correct = easy1 + easy2
    if answer == correct:
        print("Well done")
def normalAddition():
    answer = int(input(f"What is {easy1} + {easy2}?"))
    correct = easy1 + easy2
    if answer == correct:
        print("Well done")
def hardAddition():
    answer = int(input(f"What is {easy1} + {easy2}?"))
    correct = easy1 + easy2
    if answer == correct:
        print("Well done")

def subtraction():
    answer = int(input(f"What is {easy1} - {easy2}?"))
    correct = easy1 - easy2
    if answer == correct:
        print("well done")

def multiplication():
    answer = int(input(f"What is {easy1} * {easy2}?"))
    correct = easy1 * easy2
    if answer == correct:
        print("well done")

def division():
    answer = int(input(f"What is {easy1} / {easy2}?"))
    correct = easy1 / easy2
    if answer == correct:
        print("well done")

def game():
    gamemode = input("Select gamemode")
    if gamemode == "1":
        addition()
    elif gamemode == "2":
        subtraction()
    elif gamemode == "3":
        multiplication()
    elif gamemode == "4":
        division()

game()