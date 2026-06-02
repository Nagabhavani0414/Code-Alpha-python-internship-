import random

# List of words
words = ["python", "internship", "computer", "hangman", "programming"]

# Select a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check guessed word status
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if guess is correct
    if guess not in word:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

else:
    print("\n💀 Game Over!")
    print("The word was:", word)