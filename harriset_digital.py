##
# harriset_digital.py
# Ethan Harris
# 16/09/21
# Create a program that gives students math questions and offers
# an uncertain reward

def teacher_menu(SECONDS, time):
    print("Welcome to the teachers menu for Game Of Treasures!")
    teacher_choice = input("""Would you like to """)
    

def exit(SECONDS, time):
    """Redirect the user to the main menu"""
    print("Returning you to the main menu now")
    # Make the experience more natural by adding a small delay
    time.sleep(SECONDS)
    main()
    

def student_menu(difficultys, difficulty, difficult, SECONDS, time):
    """Introduce the student to the game and get them to choose
    the questions difficulty"""
    print("Welcome to the student menu")
    print("""Game of treasures is an amazingly fun math game where you
answer math questions and earn rewards!""")
    print("To start select a difficulty")
    print("Remember you can enter x at any point to exit")
    for difficult in difficultys:
        # Print out the students difficulty options
        print(difficult.title())
    while difficulty not in difficultys:
        # Ensure they have entered a valid option
        difficulty = input("What difficulty would you like?: ")
        difficulty = difficulty.lower()
        if difficulty == "x":
            # Redirect the student to the main menu if x is entered
            exit(SECONDS, time)
            break
    
    

def main():
    """Define variables and direct the user to the appropriate menu"""
    import time
    SECONDS = 0.8
    difficult = ""
    choice = ""
    choices = ["t", "s", "teacher", "student"]
    difficultys = ["easy", "medium", "hard"]
    difficulty = ""
    print("Hello and welcome to Game Of Treasures")
    while choice not in choices:
        # Ensure they can only proceed if they choose one of the two options
        choice = input("Press T for teacher menu or S for student: ".lower())
    if choice == choices[1] or choice == choices[3]:
        # Redirect to the student menu
        student_menu(difficultys, difficulty, difficult, SECONDS, time)
    elif choice == choices[0] or choice == choices[2]:
        teacher_menu(SECONDS, time)


if __name__=="__main__":
    main()
