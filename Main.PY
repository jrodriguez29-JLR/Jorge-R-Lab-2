import random


game_number = random.randint (1,10)
number_of_guesses = 0
#print (game_number)

while (True):
    guess =  int(input('Enter a number between 1 and 10: '))
    number_of_guesses = number_of_guesses + 1
    if guess > game_number:
        print('Too high')
    elif guess < game_number:
        print ('Too low')
    else:
        print('You win!')
        print ('you took',number_of_guesses,'guesses')
        break