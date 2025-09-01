import random

# here in this game you choose a number and when computer guessed the number which you chosen then feedback will be correct. otherwise high or low.

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = heigh

        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)??: ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Great! computer guessed the number, {guess}, correctly!")


guess_range = int(input("Enter a number to guess between 1 and your number: "))
computer_guess(guess_range)