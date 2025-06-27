import random
from collections import Counter
import threading
import time

# List of words
someWords = ''' honda hero tvs ola bmw ducati royalenfield 
suzuki tata ninja yamaha harleydavidson'''

someWords = someWords.split(' ')
# Randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

# Timer flag
timer_expired = False

def timer(seconds):
    global timer_expired
    time.sleep(seconds)
    timer_expired = True
    print("\nTime's up! You lost! The word was '{}'.".format(word))
    exit()

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a bike')

    for _ in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    flag = 0

    # Start the timer thread
    timer_thread = threading.Thread(target=timer, args=(60,))  # 60 seconds for the game
    timer_thread.start()

    try:
        while (chances != 0) and flag == 0:  # Flag is updated when the word is correctly guessed
            if timer_expired:
                break

            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # The guessed letter is added as many times as it occurs

            # Print the word
            word_guessed = True
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
                    word_guessed = False
            print()

            # Check if the whole word is guessed
            if word_guessed:
                flag = 1
                print('Congratulations, You won!')
                break

        # If user has used all of his chances
        if chances <= 0 and not word_guessed and not timer_expired:
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

