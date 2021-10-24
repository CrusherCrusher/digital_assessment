##
# harriset_digital.py
# Ethan Harris
# 16/09/21
# Create a program that gives students math questions and offers
# an uncertain reward

import time
import random

    

def add_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question):
    """Ask the teacher what questions they would like to add"""
    teacher_question = input("What question would you like your student to answer?: ")
    teacher_questions = eval(teacher_question)
    return teacher_question, teacher_questions
    
    
    
    
    

def multiplication_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question):
    """Ask the student a series of multiplication questions"""
    from random import randint
    print("Kia Ora and Welcome to the multiplication question menu")
    print("")
    print(f"You currently have {coins} coin" + ('s' if coins != 1 else ''))
    print("")
    print("For every question you get right you get two coins!")
    print("After getting one question right you can choose to try and double your points")
    print("")
    print("Remeber you can enter x at any point to exit")
    while len(teacher_question) > 0:
        print("")
        print("Your teacher has assigned you some questions")
        print("You cannot return to the main menu untill you have attempted all of them")
        answer = input(f"What is {teacher_question}?: ")
        try:
            # Try to turn their answer into an integer
            answer = int(answer)
        except ValueError:
             #If string is not an int this will trigger
            print(" ")
            print("Please enter a number(e.g 1, 2)")
            continue
        if answer == teacher_questions:
            print("Correct, you have earned three coins")
            coins += 3
            teacher_questions = []
            teacher_question = []
        elif answer != teacher_questions:
            print("Sorry you got that one wrong :(")
            print("Its ok you will get it right next time")
    while True:
        if coins >= 1:
            print("")
            gamble = input("Would you like to bet on you getting this next question right(y/n)?:").lower() 
        print("")
        number_one, number_two = random.randint(1, 12), random.randint(1, 12)
        answer = input(f"What is {number_one} * {number_two}?: ")
        if answer == MAIN_MENU:
            # Redirect the student to the main menu if x is entered
            exit(SECONDS, time, coins)
            break
        try:
            # Try to turn their answer into an integer
            answer = int(answer)
        except ValueError:
             #If string is not an int this will trigger
            print(" ")
            print("Please enter a number(e.g 1, 2) or x to exit")
            continue
        if answer == number_one * number_two:
            print(f"Correct, you have earned one coin" + (" and have doubled your coins" if gamble == "y" else "") + "!")
            coins += 2
            if gamble == "y":
                coins *= 2
            print(f"You now have {coins} coin" + ('s' if coins != 1 else ''))
        elif answer != number_one * number_two:
            print("Sorry you got that one wrong")
            print(f"The correct answer was {number_one * number_two}")
            if gamble == "y":
                coins /= 2
                print(f"You now have {coins} coin" + ('s' if coins != 1 else ''))
        again = input("Would you like another question?(y/n): ").lower()
        if again != "y":
            return coins

def subtraction_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question):
    """Ask the student a series of subtraction questions"""
    from random import randint
    print("Kia Ora and Welcome to the addition question menu")
    print("")
    print(f"You currently have {coins} coin" + ('s' if coins != 1 else ''))
    print("")
    print("For every question you get right you get one coin!")
    print("After getting one question right you can choose to try and double your points")
    print("")
    print("Remeber you can enter x at any point to exit")
    while len(teacher_question) > 0:
        print("")
        print("Your teacher has assigned you some questions")
        print("You cannot return to the main menu untill you have attempted all of them")
        answer = input(f"What is {teacher_question}?: ")
        try:
            # Try to turn their answer into an integer
            answer = int(answer)
        except ValueError:
             #If string is not an int this will trigger
            print(" ")
            print("Please enter a number(e.g 1, 2)")
            continue
        if answer == teacher_questions:
            print("Correct, you have earned three coins")
            coins += 3
            teacher_questions = []
            teacher_question = []
        elif answer != teacher_questions:
            print("Sorry you got that one wrong :(")
            print("Its ok you will get it right next time")
    while True:
        if coins >= 1:
            print("")
            gamble = input("Would you like to bet on you getting this next question right(y/n)?:").lower() 
        print("")
        number_one, number_two = random.randint(1, 100), random.randint(1, 100)
        answer = input(f"What is {number_one} - {number_two}?: ")
        if answer == MAIN_MENU:
            # Redirect the student to the main menu if x is entered
            exit(SECONDS, time, coins)
            break
        try:
            # Try to turn their answer into an integer
            answer = int(answer)
        except ValueError:
             #If string is not an int this will trigger
            print(" ")
            print("Please enter a number(e.g 1, 2) or x to exit")
            continue
        if answer == number_one - number_two:
            print(f"Correct, you have earned one coin" + (" and have doubled your coins" if gamble == "y" else "") + "!")
            coins += 1
            if gamble == "y":
                coins *= 2
            print(f"You now have {coins} coin" + ('s' if coins != 1 else ''))
        elif answer != number_one - number_two:
            print("Sorry you got that one wrong")
            print(f"The correct answer was {number_one + number_two}")
            if gamble == "y":
                coins /= 2
                print(f"You now have {coins} coin" + ('s' if coins != 1 else ''))
        again = input("Would you like another question?(y/n): ").lower()
        if again != "y":
            return coins
        
        

def addition_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question):
    """Ask the student a series of addition questions"""
    from random import randint
    print("Kia Ora and Welcome to the addition question menu")
    print("")
    print(f"You currently have {coins} coin" + ('s' if coins != 1 else ''))
    print("")
    print("For every question you get right you get one coin!")
    print("After getting one question right you can choose to try and double your points")
    print("")
    print("Remeber you can enter x at any point to exit")
    while len(teacher_question) > 0:
        print("")
        print("Your teacher has assigned you some questions")
        print("You cannot return to the main menu untill you have attempted all of them")
        answer = input(f"What is {teacher_question}?: ")
        try:
            # Try to turn their answer into an integer
            answer = int(answer)
        except ValueError:
             #If string is not an int this will trigger
            print(" ")
            print("Please enter a number(e.g 1, 2)")
            continue
        if answer == teacher_questions:
            print("Correct, you have earned three coins")
            coins += 3
            teacher_questions = []
            teacher_question = []
        elif answer != teacher_questions:
            print("Sorry you got that one wrong :(")
            print("Its ok you will get it right next time")
    while True:
        if coins >= 1:
            print("")
            gamble = input("Would you like to bet on you getting this next question right(y/n)?:").lower() 
        print("")
        number_one, number_two = random.randint(1, 100), random.randint(1, 100)
        answer = input(f"What is {number_one} + {number_two}?: ")
        if answer == MAIN_MENU:
            # Redirect the student to the main menu if x is entered
            exit(SECONDS, time, coins)
            break
        try:
            # Try to turn their answer into an integer
            answer = int(answer)
        except ValueError:
             #If string is not an int this will trigger
            print(" ")
            print("Please enter a number(e.g 1, 2) or x to exit")
            continue
        if answer == number_one + number_two:
            print(f"Correct, you have earned one coin" + (" and have doubled your coins" if gamble == "y" else "") + "!")
            coins += 1
            if gamble == "y":
                coins *= 2
            print(f"You now have {coins} coin" + ('s' if coins != 1 else ''))
        elif answer != number_one + number_two:
            print("Sorry you got that one wrong")
            print(f"The correct answer was {number_one + number_two}")
            if gamble == "y":
                coins /= 2
                print(f"You now have {coins} coin" + ('s' if coins != 1 else ''))
        again = input("Would you like another question?(y/n): ").lower()
        if again != "y":
            return coins
        

        

def teacher_menu(teacher_choice, teacher_choices, difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question):
    """Direct the teacher to where they need to go"""
    print("Welcome to the teachers menu for Game Of Treasures!")
    print(""" """)
    print("Remember you can enter x at any time to return to the main menu")
    print(" ")
    while teacher_choice not in teacher_choices:
        teacher_choice = input("""Would you like to add a question for your student(1)
or see your students results(2)?: """)
        teacher_choice = teacher_choice.lower()
        if teacher_choice == MAIN_MENU:
            exit(SECONDS, time)
        elif teacher_choice == teacher_choices[0]:
            teacher_question, teacher_questions = add_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question)
            return teacher_question, teacher_questions
        elif teacher_choice == teacher_choices[1]:
            print(f"Your student has collected {coins} coin" + ('s' if coins != 1 else ''))
            main()
            
            
            
            
    

def exit(SECONDS, time, coins):
    """Redirect the user to the main menu"""
    print(" ")
    print("Returning you to the main menu now")
    # Make the experience more natural by adding a small delay
    time.sleep(SECONDS)
    print(" ")
    main()
    

def student_menu(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question):
    """Introduce the student to the game and get them to choose
    the questions difficulty"""
    print(" ")
    print(" ")
    print("Welcome to the student menu")
    print(" ")
    print("""Game of treasures is an amazingly fun math game where you
answer math questions and earn rewards!""")
    print(" ")
    print("For every question you get right you get coins!")
    print("And after answering a question you can try to double your points!")
    print("Watch out though. If you try to double your points and get the next question wrong...")
    print("You lose half of your points!")
    print("")
    print("To start select a difficulty")
    print(" ")
    print("Remember you can enter x at any point to exit")
    print(" ")
        # Print out the students difficulty options
    print("""Addition = 1
Subtraction = 2
Multiplication = 3""")
    while again == True:
        # Ensure they have entered a valid option
        print(" ")
        difficulty = input("What difficulty would you like?: ")
        if difficulty == MAIN_MENU:
            # Redirect the student to the main menu if x is entered
            exit(SECONDS, time, coins)
            break
        try:
            # Attempt to turn their answer into an int
            difficulty = int(difficulty)
        except ValueError:
            # If string is not an int this will trigger
            print(" ")
            print("Please enter a number or x to exit")
            continue
        if difficulty == int(difficulty) and difficulty in difficultys:
            print("")
            print("Directing you to your selected question type now!")
            time.sleep(SECONDS)
            again = False
        elif difficulty not in difficultys:
            print("Please enter 1, 2 or 3 to continue or x to exit")
    if difficulty == difficultys[0]:
        coins = addition_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question)
        return coins
    if difficulty == difficultys[1]:
        coins = subtraction_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question)
        return coins
    elif difficulty == difficultys[2]:
        multiplication_questions(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question)
        return coins
    

def main():
    """Define variables and direct the user to the appropriate menu"""
    coins = 0
    SECONDS = 0.8
    MAIN_MENU = "x"
    choice = ""
    choices = ["t", "s", "teacher", "student"]
    difficultys = [1, 2, 3]
    difficulty = ""
    teacher_choice = ""
    teacher_choices = ["1", "2"]
    teacher_question = []
    teacher_questions = []
    answer = ""
    again = True
    number_one = 0
    number_two = 0
    gamble = ""
    while True:
        choice = ""
        print("Hello and welcome to Game Of Treasures")
        while choice not in choices:
            # Ensure they can only proceed if they choose one of the two options
            choice = input("Press T for teacher menu or S for student: ")
            choice = choice.lower()
        if choice == choices[1] or choice == choices[3]:
            # Redirect to the student menu
            coins = student_menu(difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question)
        elif choice == choices[0] or choice == choices[2]:
            teacher_question, teacher_questions = teacher_menu(teacher_choice, teacher_choices, difficultys, difficulty, SECONDS, time, MAIN_MENU, random, coins, answer, again, number_one, number_two, gamble, teacher_questions, teacher_question)


if __name__=="__main__":
    main()
