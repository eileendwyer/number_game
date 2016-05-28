import random


def number_game():
    random_num = random.randint(1,100)
    count = 0
    for count in range(1,6):
        try:
            guess = int(input("Guess a number between 1 and 100:"))
        except ValueError:
                print(" {} isn't a number ! Guess again." .format(guess))
        if  guess > random_num:
            print(" {} is too high.".format(guess))
        elif guess < random_num:
            print(" {} is too low." .format(guess))
        else:
            break
    if guess == random_num:
        print("You guessed {}, that's my number !".format(random_num))
        end_game()
    else:
        print("You didn't guess it. My number was {}.".format(random_num))
        end_game()


def end_game():
    play_again = input("Do you want to play again? y/n").lower()
    if play_again == 'y':
        number_game()
    else:
        print("Goodbye!")

number_game()









