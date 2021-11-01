# Dice Rolling Simulator
# Program randomly choose a number and print its number along with a running total
# Then will ask if you want to roll again

from random import randint

print("Would you like to roll the Dice? Type Yes or No")
user_roll = input()

total_sum = 0  # sum set to = 0

# prompt to roll dice
if user_roll == "yes":
    dice = randint(1, 6)
    print("You rolled a " + str(dice) + " this turn")
    total_sum = total_sum + dice

    # while loop until user enters no
    while True:
        print("Would you like to roll the dice again?")  # prompt to ask user to roll again
        user_roll = input()

        if user_roll == "yes":
            dice = randint(1, 6)
            print("You rolled a " + str(dice) + " this turn")
            total_sum = total_sum + dice
            print("Your running total is " + str(total_sum))

        elif user_roll == "no":
            print("Your total rolled is " + str(total_sum))
            break


# user input other than yes or no
else:
    print('Please try again, don\'t forget to watch your spelling')
