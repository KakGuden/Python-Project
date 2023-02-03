import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)

def addition():
    answer = int(input(f"What is {num1} + {num2}?"))
    correct = num1 + num2
    if answer == correct:
     print("well done")
addition()