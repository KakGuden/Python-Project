import random



def addition():
    difficulty = input("Select between Easy,Normal or Hard")
    if difficulty == "Easy":
        easyAddition()
    elif difficulty == "Normal":
        normalAddition()
    elif difficulty == "Hard":
        hardAddition()

def easyAddition():
    easy1 = random.randint(1,10)
    easy2 = random.randint(1,10)
    answer = int(input(f"What is {easy1} + {easy2}?"))
    correct = easy1 + easy2
    if answer == correct:
        print("Well done")
        nextGame = input("Press 1 to go again or 2 to switch mode")
        if nextGame == "1":
            easyAddition()
        elif nextGame == "2":
            game()

def normalAddition():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = int(input(f"What is {normal1} + {normal2}?"))
    correct = normal1 + normal2
    if answer == correct:
        print("Well done")

def hardAddition():
    hard1 = round(random.uniform(1, 100),1)
    hard2 = round(random.uniform(1, 100),1)
    answer = int(input(f"What is {hard1} + {hard2}?"))
    correct = hard1 + hard2
    if answer == correct:
        print("Well done")

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