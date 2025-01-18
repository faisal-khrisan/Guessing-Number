import random
from art import logo
#loop for asking the user if he wants to play again
restart_the_game=True
while restart_the_game:
    # creating a random number in range between 1 and 100
    random_num=random.randint(1,100)
    def choose_guess_type():
        """This function is for asking user to choose difficulty level of the guessing whether is hard or easy """
        #loop to validate the input if the user does not prompt easy or hard
        while True:
            guess_type = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
            attempts=0
            if guess_type.lower()=='hard':
                attempts=5
                break
            elif guess_type.lower()=='easy':
                attempts = 10
                break
            else:
                print("Invalid input try again")
        return attempts

    def difficulty_level(attempts_num):
        """This function is for implementing the difficulty level of the guess by giving attempts
        based on the difficulty level they chose"""
        count=attempts_num
        #loop for the attempts
        while count>0:
            print (f"You have {count} attempts remaining to guess the number.")
            guess=int(input("Make a guess:"))
            if guess==random_num:
                print (f"You go it the answer is {guess}")
                break
            elif guess>random_num:
                print("Too high !")
            else:
                print ("To low !")
            count-=1
        if count==0:
            print("You've run out of guesses.")

    #printing the logo at the head of the screen if you restart a new game, you need to enlarge the terminal to see this format
    print (logo+"\n"*12)

    print ("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_of_attempts=choose_guess_type()
    difficulty_level(number_of_attempts)
    choice=str(input("Would you like to play again type 'any letter in the keyboard' for restart and 'n' for exit the game :"))
    if choice.lower()=='n':
        restart_the_game=False
    else:
        #For cleaning the screen(terminal) for new game
        print("\n"*100)