import random
def hangman(guessed, secret):
    '''The function will create an empty string for answer which will be returned
    at the end of the function. The function has two parameters, guessed and secret.
    For each of the characters in secret, if that character is in guessed, then 
    it will add the character to answer. Else, if the character is a space, then
    a space will be added to answer. Otherwise, a dash will be added for the characters
    that have not been guessed yet. Answer will then be returned with dashes for 
    letters which haven't been identified and the characters which have been
    guessed correctly.'''
    
    print 'Welcome to our Disney Themed HANGMAN!' #prints text when game is started
    print 'Turn on ALL CAPS now'#prints text when game is started
    print 'If at anytime you would like to exit the game, type \"ABORT\"'#prints text when game is started
    print 'You only have 10 tries so guess wisely!'#prints text when game is started
    words = ['WINNIE THE POOH', 'MICKEY MOUSE', 'GOOFY', 'OLAF', 'DONALD DUCK', 
    'PLUTO', 'MALEFICENT', 'CINDERELLA'] #the code will choose one of the random words
    #to replace the secret so the user can guess the word
    secret = random.choice(words) #chooses a random word form the words list
    print secret #prints the word chosen from the previous code 
    word_found = False
    counter = 0 #represents the amount of tries taken to guess the word
    total = ''
    
    while word_found == False:
        counter += 1# this will add to the value in the counter so when it reaches 
        #10 the game will end
        print 'Turn:', counter
        guessed = raw_input('Which letter would you like to guess?  ') #this will
        #ask what letter the user is trying to guess
        user_input = ''
        if guessed == "ABORT": #when the user types ABORT it will exit the game.
            print 'You have now exited DISNEY HANGMAN'    
            break
        elif len(guessed) > 1 and guessed != secret:
            print 'Oops, you guessed more than 1 letter. Try again!'
        else:
            total += guessed
            for char in secret: # for each character in secret
                if char in total: # is character is in guessed
                    user_input += char # adds the character to answer which is currently an 
                    #empty list
                elif char == " ": # if character is a space
                    user_input += " "# adds a space to answer which is currentlly an empty list
                else:
                    user_input += "-" # the letters do not match the word so it displays a dash.
            print user_input
            if counter == 10:
                print 'Game Over'
                print "The word was ", secret
                break
            elif user_input == secret:
                word_found = True
                print "You guessed it right in ", counter, " attempts! Great Job!"
    return user_input