import random

number_to_guess = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("🎯 Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: ")

    if not guess.isdigit():
        print("⚠️ Please enter a valid number.\n")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        print("🔻 Too low!\n")
    elif guess > number_to_guess:
        print("🔺 Too high!\n")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} tries.")
        break
else:
    print(f"💥 Game Over! The number was {number_to_guess}.")