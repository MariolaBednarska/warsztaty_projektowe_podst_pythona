import random

def get_numbers():
    result = set()

    while len(result) < 6:
        try:
            numbers = input("Wytypuj 6 liczb oddzielonych spacjami: ").split()

            for number in numbers:
                number = int(number)
                if 0 < number <= 49:
                    result.add(number)

                if len(result) == 6:
                    break
            else:
                print("Nieprawidłowe liczby!")

        except ValueError:
            print("To nie jest liczba!")

    return result


def print_numbers(numbers):
    print(", ".join(str(number) for number in sorted(numbers)))


def drawing_numbers():
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return set(numbers[:6])


def lotto():
    user_numbers = get_numbers()
    print("Twoje liczby:")
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Liczby Lotto:")
    print_numbers(random_numbers)

    hits = 6 - len(random_numbers - user_numbers)

    print(f"Trafiłeś {hits} {'number' if hits == 1 else 'liczb'}!")

lotto()