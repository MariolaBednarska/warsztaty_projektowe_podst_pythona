import random

def guess_number():
    low = 1
    high = 1000
    attempt = 1

    while attempt <= 10:
        guess = random.randint(low, high)
        print(f"Computer's guess: {guess}")

        answer = input("Is it too small (s), too big (b) or you win (w)? ")

        if answer == 's':
            low = guess + 1
        elif answer == 'b':
            high = guess - 1
        elif answer == 'w':
            print("Computer wins!")
            break

        attempt += 1

    print("Computer failed to guess the number within 10 turns.")

guess_number()