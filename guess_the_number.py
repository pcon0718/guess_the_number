import random


## Keep asking until user guesses the number.
number = input("Pick a number between 1 and 10: ")
randnumber = random.randrange(1, 11)

## Convert user input to integer.
number = int(number)

## Print numbers:
print(f"My number: {randnumber}.")
print(f"Your guess: {number}.")

if number == randnumber:
    print("You guessed my number!")
else:
    print("Try again.")
