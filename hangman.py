from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words).upper() # randomly chooses something form the list
    while '-' in word or ' ' in word: # this loop says loop until getting a valid word without space (' ') or hyphen (-)
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) # all alphabet (A to Z)
    used_letters = set() # what the user has guessed


    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away a life if wrong
                print("Letters is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You died, sorry. The word was '%s'" % word)
    else:
        print("Congrats!! You guessed the word '%s' !!" % word)


hangman()