# import random
# randNumber = random.randint(1, 100)
# print(randNumber)
# userGuess = None
# guesses = 0

# while(userGuess != randNumber):
#     userGuess = int(input("Enter your guess: "))
#     guesses += 1
#     if(userGuess==randNumber):
#         print("You guessed it right!")
#     else:
#         if(userGuess>randNumber):
#             print("You guessed it wrong! Enter a smaller number")
#         else:
#             print("You guessed it wrong! Enter a larger number")

# print(f"You guessed the number in {guesses} guesses")
# with open("hiscore.txt", "r") as f:
#     hiscore = int(f.read())

# if(guesses<hiscore):
#     print("You have just broken the high score!")
#     with open("hiscore.txt", "w") as f:
#         f.write(str(guesses))


import random

randnumber = random.randint(1, 100)
print(randnumber)
userGuess = None
guesses = 0

while(userGuess !=randnumber):
    userGuess =  int(input("enter you guess: "))
    guesses += 1
    if (userGuess== randnumber):
        print("your guess is right")

    else:
        if (userGuess>randnumber):
            print("your guess is wrong ! enter the smallest value")
        else:    
            print("your guess is wrong ! enter the largest value")

print(f"you guessed the num in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))

    

    