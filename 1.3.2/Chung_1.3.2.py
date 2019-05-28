def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip

def hyp(leg1, leg2):
    '''Returns the length of the hypotenuse of a right triangle.'''
    c = leg1**2 + leg2**2
    c = c**0.5
    return c
    
def mean(a,b,c):
    '''Returns the mean of three numbers.'''
    result= a+b+c
    result= result/3.0
    return result
    
def perimeter(base, height):
    '''Returns the perimeter of a rectangle with side lengths base and height.'''
    p= (base+height)*2
    return p
    

#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)