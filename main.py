import random

def guess(x):
    a= True
    random_number = random.randint(1, x)
    # print(random_number)
    while a:
        guesNumber = int(input("Guess a number between 1 and " + str(x) + ":"))
        if guesNumber < random_number:
            print("Sorry, guess again. Too low")
        elif guesNumber > random_number:
            print("Sorry, guess again. Too high")
        elif guesNumber == random_number:
            print("Kudos! you have guessed the number " + str(random_number) + " correctly ")
            a = False

guess(20)