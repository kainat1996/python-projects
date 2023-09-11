# make a program that allows the user to choose any random number, if the user guesses the number higher than the actual number, the program should display "lower number please",
# if the user guesses the higher number display "higher number please ". and when the user guesses the correct number it must display how many guesses the player used to arrive at the number.


# firstly we will import random module 
import random
randNumber = random.randint(1, 100)
userGuess = None
guesses=0

# i am using this while loop because we can execute a set of statements as long as the condtion is true
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
# here we using if statement again because our program requires to show high and low number statements.
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
# it will tell us how many time user guesses to reach the actual number
print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
# it will make a new document file where it will show us the high score
if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
 