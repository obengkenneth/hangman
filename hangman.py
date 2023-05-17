
from random import choice

words = ["tree", "basket", "chair", "paper", "food", "mother", "father","menu", "hair",'pencil', "dog"]
word = choice(words)
guessed, lives, numberOfGuesses = [], 10, 0
guesses = ["_"] * len(word)
print("*" * 80)
print("\tWelcome to the Word Guessing Game popularly known as Hangman! \t")
print("*" * 80)
# print(guesses)

# main game loop
while True:
    if word == ''.join(guesses):
        print("Hurray! You are a word champion!!")
        print(f"The word you guessed is {word}!")
        print(f"It took you {numberOfGuesses} guesses.")
        print("\tThank you for playing the Hangman!\t")
        break
    hiddenWord = "".join(guesses)
    print(f"Your guessed letters : {guessed}")
    print(f"Word to guess : {hiddenWord}")
    print(f"Lives : {lives}")
    ans = input("Type quit or guess a letter : ").lower()
    numberOfGuesses += 1
    if ans == "quit":
        print("Thanks for playing.")
        break
    elif ans in word:
        print("You guessed correctly!")
        for i in range(len(word)):
            if word[i] == ans:
                guesses[i] = ans
    else:
        lives -= 1
        print("Incorrect, you lost a life.") 
        if ans not in guessed:
            guessed.append(ans)
        if lives <= 0:
            print("You lost all your lives! Try again next time.")
            break