import random



def addition():
    difficulty = input("Select between Easy,Normal or Hard")
    if difficulty == "Easy":
        easyAddition()
    elif difficulty == "Normal":
        normalAddition()
    elif difficulty == "Hard":
        hardAddition()
    else:
        print("Please enter a valid option")
        addition()

def easyAddition():
    easy1 = random.randint(1,10)
    easy2 = random.randint(1,10)
    answer = int(input(f"What is {easy1} + {easy2}?"))
    correct = easy1 + easy2
    if answer == correct:
        print("Well done")
        easyAdditionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easyAdditionOver()

def easyAdditionOver():
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
        normalAdditionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalAdditionOver()

def normalAdditionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        normalAddition()
    elif nextGame == "2":
        game()

def hardAddition():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = int(input(f"What is {hard1} + {hard2}?"))
    correct = hard1 + hard2
    if answer == correct:
        print("Well done")
        hardAdditionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardAdditionOver()

def hardAdditionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        hardAddition()
    elif nextGame == "2":
        game()

def subtraction():
    difficulty = input("Select between Easy,Normal or Hard")
    if difficulty == "Easy":
        easySubtraction()
    elif difficulty == "Normal":
        normalSubtraction()
    elif difficulty == "Hard":
        hardSubtraction()
    else:
        print("Please enter a valid option")
        subtraction()

def easySubtraction():
    easy1 = random.randint(1,10)
    easy2 = random.randint(1,10)
    answer = int(input(f"What is {easy1} - {easy2}?"))
    correct = easy1 - easy2
    if answer == correct:
        print("Well done")
        easySubtractionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easySubtractionOver()

def easySubtractionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        easySubtraction()
    elif nextGame == "2":
        game()

def normalSubtraction():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = int(input(f"What is {normal1} - {normal2}?"))
    correct = normal1 - normal2
    if answer == correct:
        print("Well done")
        normalSubtraction()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalSubtraction()

def normalSubtractionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        normalSubtraction()
    elif nextGame == "2":
        game()

def hardSubtraction():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = int(input(f"What is {hard1} - {hard2}?"))
    correct = hard1 - hard2
    if answer == correct:
        print("Well done")
        hardSubtractionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardSubtractionOver()

def hardSubtractionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        hardSubtraction()
    elif nextGame == "2":
        game()



def division():
    difficulty = input("Select between Easy,Normal or Hard")
    if difficulty == "Easy":
        easyDivision()
    elif difficulty == "Normal":
        normalDivision()
    elif difficulty == "Hard":
        hardDivision()
    else:
        print("Please enter a valid option")
        division()

def easyDivision():
    easy1 = random.randint(1,10)
    easy2 = random.randint(1,10)
    answer = int(input(f"What is {easy1} / {easy2}?"))
    correct = easy1 / easy2
    if answer == correct:
        print("Well done")
        easyDivisionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easyDivisionOver()

def easyDivisionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        easyDivision()
    elif nextGame == "2":
        game()

def normalDivision():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = int(input(f"What is {normal1} / {normal2}?"))
    correct = normal1 / normal2
    if answer == correct:
        print("Well done")
        normalDivision()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalDivision()

def normalDivisionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        normalDivision()
    elif nextGame == "2":
        game()

def hardDivision():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = int(input(f"What is {hard1} / {hard2}?"))
    correct = hard1 / hard2
    if answer == correct:
        print("Well done")
        hardDivisionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardDivisionOver()

def hardDivisionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode")
    if nextGame == "1":
        hardDivision()
    elif nextGame == "2":
        game()



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
    else:
        print("Please enter a valid option")
        game()
game()