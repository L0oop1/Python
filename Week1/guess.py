import random

# All the words
words = ["cool", "github", "2026", "trains"]

# Shhh...
best_word = ["L0oop", "l0oop"]

# Making it random
sec_word = random.choice(words)

# The trys
trys = 0

# Telling you to guess that bad, bad, bad word
while True:
        guess = input("Guess the word i'm thinking of (or 'e' to exit): ").lower()

        # Add 1 every time you try
        trys += 1

        if guess == "e":
            print("---L0oop1---")
            break # Exited

        if guess in best_word:
            print("That was wrong, but you're cool.")
            break
        elif guess == sec_word:
            print(f"Yes, good job. You did it in '{trys}' try(s)")
            break
        else:
            print("Wrong, try again")

print("---L0oop1---")
