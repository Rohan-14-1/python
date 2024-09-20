import random

def generate_secret_number():
    """Generate a 4-digit secret number."""
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return ''.join(digits[:4])

def count_cows_and_bulls(secret_number, guess):
    """Count cows and bulls."""
    cows = 0
    bulls = 0
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return cows, bulls

def main():
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to the Cows and Bulls Game!")
    print("Try to guess the 4-digit number.")
    print("For every correct digit in the correct place, you get a 'bull',")
    print("For every correct digit in the wrong place, you get a 'cow'.")
    print("Let's begin!")

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a 4-digit number.")
            continue

        cows, bulls = count_cows_and_bulls(secret_number, guess)

        if bulls == 4:
            print(f"Congratulations! You've guessed the number '{secret_number}' correctly in {attempts} attempts!")
            break
        else:
            print(f"{cows} cows, {bulls} bulls. Try again!")

if __name__ == "__main__":
    main()
