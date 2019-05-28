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
    
    print 'Welcome to our Disney Themed HANGMAN!'
    print 'Turn on ALL CAPS now'
    print 'If at anytime you would like to exit the game, type \"ABORT\"'
    words = ['Winnie the Pooh', 'Mickey Mouse', 'Goofy']
    secret = random.choice(words)
    print secret
    word_found = False
    counter = 0
    
        if 'abo'
        counter += 1
        guessed = raw_input('Which letter would you like to guess?  ')
        if 'ABORT' in guessed:
            exit
        total += guessed
        user_input = ''
        for char in secret: # for each character in secret
            if char in total: # is character is in guessed
                user_input += char # adds the character to answer which is currently an 
                #empty list
            elif char == " ": # if character is a space
                user_input += " "# adds a space to answer which is currentlly an empty list
            else:
                user_input += "-" # the letters do not match the word so it displays a dash.
        print user_input
        if user_input == secret:
            word_found = True
            print "You guessed it right in ", counter, " attempts"
    return user_input

