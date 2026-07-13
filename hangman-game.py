import random

heroes = ["ironman" , "captain" , "thor" , "hulk" , "spiderman"]

word = random.choice(heroes)

guessed = []
attempt = 6

print("="*30)
print("Welcome to the Hangman Game!")
print("="*30)

while attempt > 0 :

    display = ""
    for letter in word :
        if letter in guessed :
            display += letter + ""
        else :
            display += "_ "

    print(f"\nWord : {display}") 
    if display == word :
        print("Congratulations, You won!") 
        break

    guess = input("Guess a letter of you fav hero name : ").lower()

    if guess in guessed :
        print("You already guessed that letter.Try again!")
        continue
    
    if len(guess) != 1 or guess.isalpha() == False :
        print("Please enter a single letter")
        continue
    
    guessed.append(guess)

    if guess not in word :
        attempt -= 1
        print(f"Wrong guess! You have \"{attempt}\" attempts left.")
    else :
        print("Good guess!")

else :
    print (f"Sorry, you lost! The correct word was '{word}'.")