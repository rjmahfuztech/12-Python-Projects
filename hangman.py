from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something form the list
    while '-' in word or ' ' in word: # this loop says loop until getting a valid word without space (' ') or hyphen (-)
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) # all alphabet (A to Z)
    used_letters = set() # what the user has guessed

hangman()