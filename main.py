import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

max_points = 5 
current_points = 0  
number_of_question = 0

questions = [
    "What is the capital of Germany?", 
    "How many people live in Germany?", 
    "How many states does Germany have?", 
    "Who was the first man on the moon?", 
    "Where does anime come from?"
]

right_answers = ["berlin", "82 million", "16", "neil armstrong", "japan"]

input("Welcome to a normal test. Press Enter to continue.")
clear_console()

while True:
    if number_of_question >= max_points:
        print(f"You have answered all questions. Your final score is {current_points}/{max_points}.")
        choice = input("If you want to close the game, type 2 in. Press Enter to continue: ")
        if choice == "2":
            break
        else:
            current_points = 0
            number_of_question = 0
            clear_console()
            continue

    choice = input("Press 1 to start the game. Press 2 to leave and end this program: ")

    if choice == "2":
        break
    elif choice == "1":
        input("Good luck! Press Enter to continue.")
        clear_console()
        while number_of_question < max_points:
            number_of_question += 1
            question = f"{number_of_question}. question: {questions[number_of_question - 1]}"
            guess = input(question).lower()
            if guess == right_answers[number_of_question - 1].lower():
                input("Good job! Press Enter to continue.")
                current_points += 1
                clear_console()
            else:
                input(f"Wrong! The right answer is {right_answers[number_of_question - 1]}. Your answer was {guess}. Press Enter to continue.")
                clear_console()
    else:
        print("Wrong input! Please press 1 or 2.")

print("Goodbye!")
