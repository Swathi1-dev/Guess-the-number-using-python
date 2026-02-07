import random #importing required libraries
print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

lower=int(input("Enter the lower bond!\n")) #lowwer value
higher=int(input("Enter the higher bound!:\n")) #higher value

random_guess=random.randint(lower,higher) #random guess using random 
chances=7 #number of chances
guess_counter=0 # guess chances

while guess_counter<chances: #checking if guess counter is lesser then chances
    guess_counter+=1
    guess=int(input("Guess the number:\n"))
    
    if guess == random_guess:
        print(f"Your are correct! the num {guess} is correct and you have achieved it in {guess_counter} counts")
        break
    elif guess_counter>=chances and guess!=random_guess:
        print(f"Sorry! the number was {random_guess},better luck next time")
    elif guess > random_guess:
        print("You are wrong , you have guessed too high")
    else:
        print("You are wrong , you have guessed too low")
    