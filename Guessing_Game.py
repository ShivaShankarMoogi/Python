from random import randint
random_number_to_guess = randint(1, 20)

chances = 3
while chances > 0:
    guess = int(input("Enter your number between 1 and 20 : "))

    if guess == random_number_to_guess:
        print("You have Guessed Successfully. Congratulations! ")
        break
    elif guess < random_number_to_guess:
        print("A low Number")
    else:
        print(" A High Number ")

    chances = chances-1
    if chances >0:
        print("You have", chances, "chance(s) left.\n")
    else:
        print("Game Over, Bad luck Try Again! ")
        print("Correct Number is :",random_number_to_guess)
