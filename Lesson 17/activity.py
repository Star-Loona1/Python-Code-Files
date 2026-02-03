import random
playing = True
number = int(random.randint(10, 20))

print("I will generate a random number between 10 and 20, you will give me a number one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
    guess = int(input("Give an integer between 10 and 20: \n"))
    if number == guess:
        print("You have won the game")
        print("The number was ", number)
        break
    elif guess < number:
        print(guess, " is less than the number.")
    else:
        print("That's not quite right \nTry again")