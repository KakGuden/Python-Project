import random

def addition():
    difficulty = input("Select between Easy,Normal or Hard:\n")
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
    answer = int(input(f"What is {easy1} + {easy2}?:\n"))
    correct = easy1 + easy2
    if answer == correct:
        print("Well done")
        easyAdditionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easyAdditionOver()

def easyAdditionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        easyAddition()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        easyAdditionOver()

def normalAddition():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = int(input(f"What is {normal1} + {normal2}?:\n"))
    correct = normal1 + normal2
    if answer == correct:
        print("Well done")
        normalAdditionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalAdditionOver()

def normalAdditionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        normalAddition()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        normalAdditionOver()

def hardAddition():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = float(input(f"What is {hard1} + {hard2}?:\n"))
    correct = hard1 + hard2
    if answer == correct:
        print("Well done")
        hardAdditionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardAdditionOver()

def hardAdditionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        hardAddition()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        hardAdditionOver()

def subtraction():
    difficulty = input("Select between Easy,Normal or Hard:\n")
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
    answer = int(input(f"What is {easy1} - {easy2}?:\n"))
    correct = easy1 - easy2
    if answer == correct:
        print("Well done")
        easySubtractionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easySubtractionOver()

def easySubtractionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        easySubtraction()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        easySubtractionOver()

def normalSubtraction():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = int(input(f"What is {normal1} - {normal2}?:\n"))
    correct = normal1 - normal2
    if answer == correct:
        print("Well done")
        normalSubtractionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalSubtractionOver()

def normalSubtractionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        normalSubtraction()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        normalSubtractionOver()

def hardSubtraction():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = float(input(f"What is {hard1} - {hard2}?:\n"))
    correct = round(hard1 - hard2,1)
    if answer == correct:
        print("Well done")
        hardSubtractionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardSubtractionOver()

def hardSubtractionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        hardSubtraction()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        hardSubtractionOver()

def multiplication():
    difficulty = input("Select between Easy,Normal or Hard:\n")
    if difficulty == "Easy":
        easyMultiplication()
    elif difficulty == "Normal":
        normalMultiplication()
    elif difficulty == "Hard":
        hardMultiplication()
    else:
        print("Please enter a valid option")
        multiplication()

def easyMultiplication():
    easy1 = random.randint(1,10)
    easy2 = random.randint(1,10)
    answer = float(input(f"What is {easy1} x {easy2}?:\n"))
    correct = round(easy1 * easy2,2)
    if answer == correct:
        print("Well done")
        easyMultiplicationOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easyMultiplicationOver()

def easyMultiplicationOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        easyMultiplication()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        easyMultiplicationOver()

def normalMultiplication():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = float(input(f"What is {normal1} x {normal2}?:\n"))
    correct = round(normal1 * normal2,2)
    if answer == correct:
        print("Well done")
        normalMultiplicationOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalMultiplicationOver()

def normalMultiplicationOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        normalMultiplication()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        normalMultiplicationOver()

def hardMultiplication():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = float(input(f"What is {hard1} x {hard2}?:\n"))
    correct = round(hard1 * hard2,2)
    if answer == correct:
        print("Well done")
        hardMultiplicationOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardMultiplicationOver()

def hardMultiplicationOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        hardMultiplication()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        hardMultiplicationOver()

def division():
    difficulty = input("Select between Easy,Normal or Hard:\n")
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
    answer = float(input(f"What is {easy1} / {easy2}?:\n"))
    correct = round(easy1 / easy2,2)
    if answer == correct:
        print("Well done")
        easyDivisionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easyDivisionOver()

def easyDivisionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        easyDivision()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        easyDivisionOver()

def normalDivision():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = float(input(f"What is {normal1} / {normal2}?:\n"))
    correct = round(normal1 / normal2,2)
    if answer == correct:
        print("Well done")
        normalDivisionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalDivision()

def normalDivisionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        normalDivision()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        normalDivisionOver()

def hardDivision():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = float(input(f"What is {hard1} / {hard2}?:\n"))
    correct = round(hard1 / hard2,2)
    if answer == correct:
        print("Well done")
        hardDivisionOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardDivisionOver()

def hardDivisionOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        hardDivision()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        hardDivisionOver()



def endless():
    difficulty = input("Select between Easy,Normal or Hard:")
    if difficulty == "Easy":
        easyEndless()
    elif difficulty == "Normal":
        normalEndless()
    elif difficulty == "Hard":
        hardEndless()
    else:
        print("Please enter a valid option")
        endless()

def easyEndless():
    easy1 = random.randint(1,10)
    easy2 = random.randint(1,10)
    answer = int(input(f"What is {easy1} + {easy2}?:\n"))
    correct = easy1 + easy2
    if answer == correct:
        easy1 = random.randint(1,10)
        easy2 = random.randint(1,10)
        answer = int(input(f"What is {easy1} - {easy2}?:\n"))
        correct = easy1 - easy2
        if answer == correct:
            easy1 = random.randint(1,10)
            easy2 = random.randint(1,10)
            answer = float(input(f"What is {easy1} x {easy2}?:\n"))
            correct = round(easy1 * easy2,2)
            if answer == correct:
                easy1 = random.randint(1,10)
                easy2 = random.randint(1,10)
                answer = float(input(f"What is {easy1} / {easy2}?:\n"))
                correct = round(easy1 / easy2,2)
                if answer == correct:
                    easyEndless()
                else:
                    print("Incorrect, the right answer was")
                    print(correct)
                    easyEndlessOver()
            else:
                print("Incorrect, the right answer was")
                print(correct)
                easyEndlessOver()
        else:
            print("Incorrect, the right answer was")
            print(correct)
            easyEndlessOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        easyEndlessOver()
        
def easyEndlessOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        easyEndless()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        easyEndlessOver()

def normalEndless():
    normal1 = random.randint(11,111)
    normal2 = random.randint(11,111)
    answer = int(input(f"What is {normal1} + {normal2}?:\n"))
    correct = normal1 + normal2
    if answer == correct:
        normal1 = random.randint(11,111)
        normal2 = random.randint(11,111)
        answer = int(input(f"What is {normal1} - {normal2}?:\n"))
        correct = normal1 - normal2
        if answer == correct:
            normal1 = random.randint(11,111)
            normal2 = random.randint(11,111)
            answer = float(input(f"What is {normal1} x {normal2}?:\n"))
            correct = round(normal1 * normal2,2)
            if answer == correct:
                normal1 = random.randint(11,111)
                normal2 = random.randint(11,111)
                answer = float(input(f"What is {normal1} / {normal2}?:\n"))
                correct = round(normal1 / normal2,2)
                if answer == correct:
                    normalEndless()
                else:
                    print("Incorrect, the right answer was")
                    print(correct)
                    normalEndlessOver()
            else:
                print("Incorrect, the right answer was")
                print(correct)
                normalEndlessOver()
        else:
            print("Incorrect, the right answer was")
            print(correct)
            normalEndlessOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        normalEndlessOver()
        
def normalEndlessOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        normalEndless()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        normalEndlessOver()

def hardEndless():
    hard1 = round(random.uniform(11,111),1)
    hard2 = round(random.uniform(11,111),1)
    answer = float(input(f"What is {hard1} + {hard2}?:\n"))
    correct = round(hard1 + hard2,1)
    if answer == correct:
        hard1 = round(random.uniform(11,111),1)
        hard2 = round(random.uniform(11,111),1)
        answer = float(input(f"What is {hard1} - {hard2}?:\n"))
        correct = round(hard1 + hard2,1)
        if answer == correct:
            hard1 = round(random.uniform(11,111),1)
            hard2 = round(random.uniform(11,111),1)
            answer = float(input(f"What is {hard1} x {hard2}?:\n"))
            correct = round(hard1 * hard2,2)
            if answer == correct:
                hard1 = round(random.uniform(11,111),1)
                hard2 = round(random.uniform(11,111),1)
                answer = float(input(f"What is {hard1} / {hard2}?:\n"))
                correct = round(hard1 / hard2,2)
                if answer == correct:
                    hardEndless()
                else:
                    print("Incorrect, the right answer was")
                    print(correct)
                    hardEndlessOver()
            else:
                print("Incorrect, the right answer was")
                print(correct)
                hardEndlessOver()
        else:
            print("Incorrect, the right answer was")
            print(correct)
            hardEndlessOver()
    else:
        print("Incorrect, the right answer was")
        print(correct)
        hardEndlessOver()
        
def hardEndlessOver():
    nextGame = input("Press 1 to go again or 2 to switch mode:\n")
    if nextGame == "1":
        hardEndless()
    elif nextGame == "2":
        game()
    else:
        print("Please select a valid option")
        hardEndlessOver()

def game(): 
    print("All text inputs needs to be capitalized")
    print("Addition, Subtraction, Multiplication, Division, Endless")
    gamemode = input("Select gamemode:\n")
    print("All answers are rounded to the second decimal")
    print("Decimal numbers are writen with a . insted of a ,")
    if gamemode == "Addition":
        addition()
    elif gamemode == "Subtraction":
        subtraction()
    elif gamemode == "Multiplication":
        multiplication()
    elif gamemode == "Division":
        division()  
    elif gamemode == "Endless":
        endless()
    else:
        print("Please enter a valid option")
        game()
game()