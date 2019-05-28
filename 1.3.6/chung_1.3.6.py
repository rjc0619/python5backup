'''Part I: Tuples, Syntax'''
#1-3. N/A
#4. (2,4,6,8)
#5. underscores
#6a. the output of some_values[1] is gpomg tp be 'b' because it is the character
#in the 1st place.
#6b. the output for some_values [0:2] would be ('a', 'b') because is is asking 
#for what is in the 0th place to the 2nd place not counting the 2nd place.
#7. the output of b[1] == 10 would be true because the 10 is in the first place of 
#the list but in b[1] it would be 15 because previously a was set to 15 so when you
#input b[1] the output would be 15

'''Part II: List'''
#8. the ouput for values [1:] would be ['b', 3] because it is going from the 1st 
#character to the last one
#9. the output for values [2] == 3 is going to be false because values [2] was set
#to a string and the values [2] is checking for an interger
#10a. the output for values = values + [4, 5] would be ['a', 'b', '3', 4, 5] because
#the code is adding 4 and 5 to the list.
#10b. the output for values.append([6, 7]) would be ['a', 'b', '3', 4, 5, [6, 7]]
#because the code is adding a list to the list.
#11 this doesnt work because the list can only concatenate list (not "int") to a list
#12 A was set to 6 so what ever the code told it to be mutiplied, in this case
#3 then you would get your output which is 18.
#13 N/A

'''Part III: Lists and the random module'''
#14
import random
def roll_two_dice():
    one_dice = random.randint(1,6)
    two_dice = random.randint(1,6)
    return one_dice + two_dice
    
'''Conclusion'''
#1. A is a string, B is a tuple, and C is a list.
#2. Computer programing languages need to have a variety of variables because some
#things can be represented as intergers such as animals, fruits, and many other 
#physical things
#3. We larened about returning results from the code, using if, else, and else if.
# We also learned about nesting, tuples, list, syntax, and importing random.
#1.3.6 Function Test
print(roll_two_dice())
    
#assignment check. after running the code since the code is suppose to display a
# random number. the code will add two random numbers that are chosen from 1-6
#and that number will be displayed.