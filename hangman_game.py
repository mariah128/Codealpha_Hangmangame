import random

# List of predefined words
words = ["apple", "tiger", "python", "school", "flower"]

# Randomly choose one word
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===================================")
print("      Welcome to Hangman Game")
print("===================================")

while wrong_guesses < max_wrong:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check duplicate guess
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        print("Wrong!")
        wrong_guesses += 1

    # Check if player guessed all letters
    finished = True

    for letter in secret_word:
        if letter not in guessed_letters:
            finished = False
            break

    if finished:
        print("\nCongratulations!")
        print("You guessed the word:", secret_word)
        break

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
