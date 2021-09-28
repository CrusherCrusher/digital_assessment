##
# harriset_digital.py
# Ethan Harris
# 16/09/21
# Create a program that gives students math questions and offers
# an uncertain reward

def teacher_menu(SECONDS, time, teacher_choices, teacher_choice, MAIN_MENU):
    """Direct the teacher to where they need to go"""
    print("Welcome to the teachers menu for Game Of Treasures!")
    print(""" """)
    print("Remember you can enter x at any time to return to the main menu")
    print(" ")
    while teacher_choice not in teacher_choices:
        teacher_choice = input("""Would you like to add a question for your student(1)
or see your students results(2)?: """)
        teacher_choice = teacher_choice.lower()
        print(teacher_choice)
        if teacher_choice == MAIN_MENU:
            exit(SECONDS, time)
            
    

def exit(SECONDS, time):
    """Redirect the user to the main menu"""
    print(" ")
    print("Returning you to the main menu now")
    # Make the experience more natural by adding a small delay
    time.sleep(SECONDS)
    print(" ")
    main()
    

def student_menu(difficultys, difficulty, difficult, SECONDS, time, MAIN_MENU):
    """Introduce the student to the game and get them to choose
    the questions difficulty"""
    print(" ")
    print(" ")
    print("Welcome to the student menu")
    print(" ")
    print("""Game of treasures is an amazingly fun math game where you
answer math questions and earn rewards!""")
    print(" ")
    print("To start select a difficulty")
    print(" ")
    print("Remember you can enter x at any point to exit")
    print(" ")
        # Print out the students difficulty options
    print("""Addition = 1
Subtraction = 2
Multiplication = 3""")
    while True:
        # Ensure they have entered a valid option
        print(" ")
        difficulty = input("What difficulty would you like?: ")
        if difficulty == MAIN_MENU:
            # Redirect the student to the main menu if x is entered
            exit(SECONDS, time)
            break
        try:
            # Attempt to turn their answer into an int
            difficulty = int(difficulty)
        except ValueError:
            # If string is not an int this will trigger
            print(" ")
            print("Please enter a number or x to exit")
            continue
        if difficulty == int(difficulty):
            print("Yay")
            main()
    

def main():
    """Define variables and direct the user to the appropriate menu"""
    import time
    SECONDS = 0.8
    MAIN_MENU = "x"
    difficult = ""
    choice = ""
    choices = ["t", "s", "teacher", "student"]
    difficultys = ["1", "2", "3"]
    difficulty = ""
    teacher_choice = ""
    teacher_choices = ["a", "r"]
    print("Hello and welcome to Game Of Treasures")
    while choice not in choices:
        # Ensure they can only proceed if they choose one of the two options
        choice = input("Press T for teacher menu or S for student: ".lower())
    if choice == choices[1] or choice == choices[3]:
        # Redirect to the student menu
        student_menu(difficultys, difficulty, difficult, SECONDS, time, MAIN_MENU)
    elif choice == choices[0] or choice == choices[2]:
        teacher_menu(SECONDS, time, teacher_choices, teacher_choice, MAIN_MENU)


if __name__=="__main__":
    main()
