import random

print("Winning Rules of the following games are : \n")
print("Rock vs Paper : Paper wins\n")
print("Rock vs Scissors : Rock wins\n")
print("Paper vs Scissors : Scissors wins\n")

while True:
    print("Enter your choice : \n 1. Rock \n 2. Paper \n 3. Scissors \n")
    user_choice = int(input("Enter your choice : "))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Invalid choice, please enter a number between 1 and 3: "))

    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissors"
    
    print("User  Choice is:", user_choice_name)
    print("Now It's Computer's turn: ")

    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"
    
    print("Computer choice is:", comp_choice_name)
    print(user_choice_name, 'vs', comp_choice_name)

    if user_choice_name == comp_choice_name:
        result = "DRAW"
    elif (user_choice_name == "Rock" and comp_choice_name == "Scissors") or \
         (user_choice_name == "Paper" and comp_choice_name == "Rock") or \
         (user_choice_name == "Scissors" and comp_choice_name == "Paper"):
        result = user_choice_name
    else:
        result = comp_choice_name

    if result == "DRAW":
        print("It's a tie!")
    elif result == user_choice_name:
        print("User  wins!")
    else:
        print("Computer Wins")

    print("Do You Want to Play Again? (yes/no)")
    play_again = input().lower()
    if play_again != "yes":
        break

print("Thanks For Playing")