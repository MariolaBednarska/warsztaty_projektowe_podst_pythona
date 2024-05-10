import random


def podaj_liczbe():
    while True:
        try:
            result = int(input('Guess the number: '))
            break
        except ValueError:
            print("It's not a number!")
    return result


def guess_number():
    wylosowana_liczba = random.randint(1, 100)
    liczba_uzytkownika = podaj_liczbe()
    while liczba_uzytkownika != wylosowana_liczba:
        if liczba_uzytkownika < wylosowana_liczba:
            print("It's too small!")
        else:
            print("It's too big!")
        wylosowana_liczba = liczba_uzytkownika
    print("You win!")

guess_number()
