# # string concatenation (How to put string together)
# # Suppose we want to create a string that says "Subscribe to ______"
# youtuber = "Mahfuz Islam" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

print('''Fill in the gaps!
Computer programming is so _____! It makes me so excited all the time because I love to _____. Stay hydrated and _____ like you are _____''')

print('\nAnswer here:')

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the \
time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print('\n')
print(madlib)