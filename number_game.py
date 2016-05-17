import random
def number_game():
    random_num = random.randint(1,100)
    guesses = []

    while len(guesses) <= 5:
        try:
            guess = int(input("Guess a number between 1 and 100:"))
        except ValueError:
                print(" {} isn't a number !" .format(guess))
    else:

  if guess == random_num:
        print("You guessed {}, that's my number !".format(random_num))
        guesses.append(guess)
        break

    elif guess > random_num:
        print(" Your guess is too high.".format(guess))

    elif guess < random_number:
        print("Your guess is too low." .format(guess))
        guesses.append(guess)
  else:
      print("You didn't guess it. My number was {}.".format(random_num))
      play_again = input("Do you want to play again? y/n")
  if play_again = 'y':
      number_game()
  else:
      print("Goodbye!")



