'''Part I: for loops, range(), and help()'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

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
    a += [random.choice([2,3,4,5,6,7,8,9,10,11,12])]
    for choices in range(100):
            a += [random.choice([2,3,4,5,6,7,8,9,10,11,12])]

    plt.hist(a)
    plt.savefig('1.3.7/roll_hundred_pair')
    
def dice(n):
    a = []
    a += [random.choice([2,3,4,5,6,7,8,9,10,11,12])]
    for choices in range(100):
            a += [random.choice([2,3,4,5,6,7,8,9,10,11,12])]
