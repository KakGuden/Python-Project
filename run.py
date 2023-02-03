import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)

def addition():
    answer = int(input(f"What is {num1} + {num2}?"))
    correct = num1 + num2
    if answer == correct:
        print("well done")

def subtraction():
    answer = int(input(f"What is {num1} - {num2}?"))
    correct = num1 - num2
    if answer == correct:
        print("well done")

def multiplication():
    answer = int(input(f"What is {num1} * {num2}?"))
    correct = num1 * num2
    if answer == correct:
        print("well done")

def division():
    answer = int(input(f"What is {num1} / {num2}?"))
    correct = num1 / num2
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