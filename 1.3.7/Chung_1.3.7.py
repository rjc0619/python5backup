from __future__ import print_function
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''This function is for the user to guess who the winner is and for the 
    program to return what is correct.
    
    Amy, Bill, Cathy, and Dale are the names of the "players" from which the actual
    player must guess the winner. They are strings.
    '''
    winner = random.choice(players) 
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # The index is 0 to the length of players
    # minus 1
        print(p+', ', end='')
    print(players[len(players)-1]) # This will print the item from players at the 
    # given index of the length of players minus 1.
    # The following code is related to how many guesses the player won in and if
    # they need to try again if they are wrong. If they guess again, then it 
    # adds one more to guesses and then at the end, the amount of guesses is 
    # returned
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses

'''Part I: for loops, range(), and help()'''


def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('picks')
def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
def roll_hundred_pair():
    a = []
    a += [random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])]
    for choices in range(10):
        a += [random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])]

    plt.hist(a)
    plt.savefig('1.3.7/roll_hundred_pair')
def dice(n):
    b = 0
    b = random.choice(range(n, 6*n+1))
    print ('Roll was', b) 
'''Part II: While loops'''
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
# 7. You cannot use the variable until it is initialized which is why it is 
# important to do so and you cannot use a because a is in the answer so the
# program will think that you already guessed.
def goguess():
    print('I have a number between 1 and 20 inclusive.')
    num = (random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print (num)
    guess = 0
    guesses = 0
    while guess != num:
        guess = int(raw_input('Guess: '))
        guesses += 1
        if guess < num:
            print(guess, ' is too low.')
        elif guess > num:
            print(guess, ' is too high.')
    if guess == num:
            print('Right! My number is ', guess,'! You guessed in ', guesses,'guesses!')
# 10. You will need 36,000,000 guesses to make sure you are right.

'''Part III: Practice'''
def matches(ticket, winners):
    results = 0
    for i in winners:
        if i in ticket:
            results += 1
    return results
    
def report(guess, secret):
    result = [0, 0]
    guessed = []
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            guessed.append(i)
            result[0] += 1
    for i in range(len(secret)):
        for item in range(len(guess)):
            if (not(item in guessed or i in guessed)) and secret[i]==guess[item]:
                result[1] += 1
                guessed.append(item)
    return result
        
    
    
# Conclusion 1. The disadvantages are that it is harder to find  bugs without 
# using loops and you are more likely to make mistakes.

# Conclusion 2. Iteration actually changes things whereas analysis only evaluates.

# Conclusion 3. A while loop is used is when you want someting executed after
# a certain condition. For loops are used for each and every value no matter
# the condition.

# Conclusion 4. We helped each other understand some of the functions and
# we worked together to find some solutions by combining ideas.

#1.3.7 Function Test
picks()
days()
roll_hundred_pair()
dice(5)
validate()
goguess()
print (matches([11, 12, 13, 14, 15],[14, 15, 16]))
guess = ('red', 'red', 'red', 'green', 'yellow')
secret = ('red', 'red', 'yellow', 'yellow', 'black')
print (report(guess, secret))