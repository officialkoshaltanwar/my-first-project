#now we will try to make a game with advnced three level 
import random

def advance_game():
  while True:
    print(" 🎯 Welcome to Koshal Tanwar Number Guess Game")
    print("Choose your level:")
    print("Level 1: Easy(1-50) : 10 attempts")
    print("Level 2: Medium(1-100) : 7 attempts")
    print("Level 3: Hard(1-200) : 5 attempts")

    choice = int(input("Enter your level choice(1,2,3): "))
    if choice == 1:
        max_number = 50
        attempts = 10
    elif choice == 2:
        max_number = 100
        attempts = 7
    elif choice == 3:
        max_number = 200
        attempts = 5
    else:
        print("Invalid choice. Exiting game.")
        return
    
    secret_number = random.randint(1, max_number)
    print("I have selected a number between 1 and", max_number)
    won = False

    while attempts > 0:
        guess = int(input("Enter your guess:"))
        if guess == secret_number:
            print("🎉Congratulation! You Won the game:")
            won = True
            break
        elif guess < secret_number:
            attempts -= 1
            print("Too low! Now you have only ", attempts, "attempts left")
        else:
            attempts -= 1
            print("Too high! Now you have only ", attempts, "attempts left")
            if not won:
             print("You used your all attempts. Your Number was :", secret_number)
    replay = input("Do you want to play again (Y/N)").lower()
    if replay != 'y':
        print("Be ready to play again")
        return

advance_game()