import random

def generate_secret():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(digits)
    secret = ''
    for digit in digits[:4]:
        secret += str(digit)
    return secret

def calculate_cows_and_bulls(secret, guess):
    cows = 0
    bulls = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return cows, bulls

secret = generate_secret()
while True:
    guess = input('Guess: ')
    if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
        cows, bulls = calculate_cows_and_bulls(secret, guess)
        print(f"{cows} cows, {bulls} bulls")

        if bulls == 4:
            print("You win!")
            break
    else:
        print("Invalid guess.")


