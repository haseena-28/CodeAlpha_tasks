import random

# 5 predefined words
words = ["python", "mango", "laptop", "music", "tiger"]

# Pick random word
word = random.choice(words)

guessed = []
wrong = 0

print("Welcome to Hangman!")
print("Guess the word, you have 6 wrong chances.\n")

# Game loop
while wrong < 6:

    # Show current word status
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    # Check if word is complete
    if all(letter in guessed for letter in word):
        print("\nYou Win! The word was:", word)
        break

    # User guess
    guess = input("\nEnter a letter: ").lower()

    if guess in guessed:
        print("Already guessed that letter!")

    elif guess in word:
        guessed.append(guess)
        print("Correct!")

    else:
        guessed.append(guess)
        wrong += 1
        print("Wrong! Chances left:", 6 - wrong)

else:
    print("\nYou Lose! The word was:", word)
