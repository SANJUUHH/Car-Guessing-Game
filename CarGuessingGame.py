#GAME: CAR GUESSING GAME

import random

#User inputs
name = input("Enter your name: ")
print("Hello " + name + ", Welcome to the Car Guessing Game!")
print("You have 12 chances to guess the car name.")

cars = ["range-rover", "mercedes", "lexus", "audi", "porsche", "bmw", "bugatti", "jaguar", "toyota", "rolls-royce"]
car = random.choice(cars)

print("The car name have",len(car),"characters")
print( "_ "*len(car))

print("Guess any alphabet: ")
guesses = " "

turns = 12

while turns > 0:
    failed = 0
    for char in car:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("\nYou Win")

        print("The word is: ", car)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in car:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")
        




    




