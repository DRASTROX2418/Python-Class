import random 
secret = random.randint(1,10)

print("Guess the number Beta!")
guess = int(input("Choose a number from 1 to 10:"))

if guess == secret:
    print("Ganz richtig! You won!")

else:
    print("Very close! THE number was:", secret)
    