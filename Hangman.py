import random
word_list = ["apple","tiger","chair","bread","plant"]
secret_word = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(display_word())
while wrong_guesses < max_wrong_guesses and set(guessed_letters) != set(secret_word):
    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} tries left.")
    print(display_word())
if set(secret_word).issubset(set(guessed_letters)):
    print("Congratulations! You've guessed the word:", secret_word)
else:
    print("Sorry, you ran out of guesses. The word was:", secret_word)
