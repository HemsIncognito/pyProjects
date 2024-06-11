import random
import os
import time
#print("INTRODUCTION TO THE GAME: \n\nAim: The player has to guess a random number in the range [1, 100] until guessed right.\n\tWarm means close, Cold means far away\n To EXIT press -1\n")
os.system('cls')
print("{0:>75}".format('WELCOME TO GUESS ME!'))
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("To Exit Press -1")
print("LET'S PLAY!")
num = random.randint(1, 100)
lst = [0]
count = 0
n = -1

while(n != num):
    count +=1
    n = int(input("Guess the number: "))
    lst.append(n)
    if n > 100 or n < -1:
        print('Stay In Bounds')
    elif n == -1:
        print(f"The number was {num}.\nBetter Luck next time.")
        break
    if n == num:
        if count == 1:
            print("Are you a Wizard?")
            time.sleep(1.5)
            print("Cuz' That's the number!!")
        else:
            print(f"Congratulations! U guessed the number in {count} guesses.")

    if lst[-2]:
        if abs(n - num) > abs(num - lst[-2]):
            print('Colder')
        else:
            print('Warmer')
    else:
        if n > num+10 or n < num-10:
            print("Cold")
        else:
            print("Warm")
    
