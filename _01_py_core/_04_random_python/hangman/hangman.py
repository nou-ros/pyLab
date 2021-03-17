'''
word - the word we are looking for
allowed_errors - number of errors allowed 
guessed - list of guessed letter
'''
import random

# choosing a random word from the text file
with open('wordlist.txt', 'r') as f:
    words = f.readlines()

# readline will return an extra \n at the end of each line so we have to remove it. 
word = random.choice(words)[:-1]

allowed_errors = 7
guessed = []

done = False

while not done:
    for letter in word:
        if letter.lower() in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Errors left: {allowed_errors}\nGuess a letter: ")
    guessed.append(guess.lower())
    allowed_errors -= 1
    
    guessed_word = ''.join(str(l) for l in guessed) 

    if allowed_errors==0:
        done = True
        print(f'Game Over! The word was: {word}')
    elif guessed_word == word:
        print(f"Congratulations, you guessed correctly. The word was: {word}")
        done = True
        
