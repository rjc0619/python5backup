from __future__ import print_function
import random
'''Part I. Nested if structures and testing'''

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1a. the return value resutled from line 17
# 1bi. orange
# 1bii. apple
# 1biii. potato
# 1biv. mango
# 1c. because bananas are a fruit then it will not be true because it checks of it it NOT a fruit and is starchy.
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food id()'
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
# Assignment 3
def f(n):
        if int(n)==n:
            if n % 2 == 0:
                if n % 3 == 0:
                    print (n, "is odd")
                else:
                    print (n, "is even")
                if n % 2 == 0 and n % 3 == 0:
                        print (n, "is a mutiple of 6")
        else:
            if n % 2 != 0 and n % 3 != 0:
                print ("n is not an interger")
#5. You need four numbers: a non-integer, any odd number, any multiple of 6, and 
#any even number that is not a multiple of 6. For example: 1.5, 7, 12, and 10.
def f_test():
    works = True
    if f(2) !=  'the number is an interger, even':
        works = 'it is not an interger, odd'
    if f(2.4) !=  'the number is not an interger':
        works = 'it is an interger' 
    if f(3) !=  'the number is an interger, odd':
        works = 'it is not an interger, even'
        works == True
        print("All good!")
        return True
    else:
        print(works)
        return False
    
#7 When the + operator is between two strings, it concatenates, putting the second
#string of characters right after the first string of characters and into a single
#concatenated string. When the + operator is between two numbers, it performs 
#numeric addition, resulting in an int or float.

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print('Too low, my number was,', secret, '.', sep='')
    else:
        print('Too high, my number was,', guess, '.', sep='')
def quiz_decimal(low, high):
    
        
    #if guess = secret:
       # print('Right on, my number is', guess, end='!\n' )
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
#quiz_decimal(4, 4.1)
#quiz_decimal(4, 4.1)
#f_challenge(1.1)
#f_challenge(2)
#f_challenge(3)
#f_challenge(6)
