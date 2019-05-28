from __future__ import print_function # use Python 3.0 printing
''' Part 1 Conditionals '''

 #6a. prediction: a=3 because 3 squared equals 9 and also 3 is not greater than 
 #  3 and it is true.
 #  my prediction was correct
 
 #6b. prediction True because 3 plus 2 is 5 and also 3 minus 1 doesn't equal 3
 #  my prediction was correct
 
 #7 in the terminal
 
 #8 in the terminal
 
'''Part II: if-else Structures & the print() Function!!!!'''
def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)

def report_grade(percent):
    '''Step 9b if-else'''
    if percent >= 80:
        print(percent, 'Keep up the good work!')
    else:
        print(percent, 'Seek extra practice or help.')
        
'''Part III. The in operator and an introduction to collection'''

#10 True and False
#11 code:
def letter_in_word (guess, word):
    if guess in word:
        return True
    else:
        return False 
def hint (color, secret):
    if color in secret:
        print('The color', color, 'IS in the secret sequence of colors.')
    else:
        print('The color', color, 'IS NOT in the secret sequence of colors.')

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

        