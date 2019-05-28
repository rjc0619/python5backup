'''introduction'''
#1-4. N/A
#5. int and long
#6. the first one works out bt the second one doen't work because you cant add an
# an interger to a string.
#7 The data is asking for the letter that is in the 0th place. If there is a 
#then is is the number to the last. If there is more then the amount of characters
#there are then it will display a error unless it is defined and told what to do
#8-9. N/A
#10a. the output of len(activity) will be the lenght of theater which is 7
#10b. the output would be theate because you are taking one character away from the
#activity
#11. the data is checking if "test goo" is in the statment and if it is then it
#will display a true but if no then it will display a false.
def how_eligible(essay):
    add=0
    if '?' in essay:
        add += 1
    if '"' in essay:
        add += 1
    if ',' in essay:
        add += 1
    if '!' in essay:
        add += 1
    return add
    
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
#Assignment Check 1. The result we got after running the code is 4 and 1. I think
#I have successfully completed the assignment because the outputs are correct.