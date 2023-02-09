import random

guesses = 0
print("Hello! What is your name?")
name = input()
number = random.randint(1, 20)
s1 = "Well, {}, I am thinking of a number between 1 and 20."
print(s1.format(name))

while guesses < 6:
    print("Take a guess.") 
    guess = input()
    guess = int(guess)
    guesses += 1
    
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        s2 = "Good job, {}! You guessed my number in {} guesses!"
        print(s2.format(name,guesses))
        break