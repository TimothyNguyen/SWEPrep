'''
Make change in quarters, dimes, nickels and pennies 
from a given number of pennies
'''
def divide_change(change):
    if change > 99:
        return 'too much'
    
    quarters, dimes, nickels, pennies = 0, 0, 0, 0
    while change > 24:
        change -= 25
        quarters += 1
    while change > 9:
        change -= 10
        dimes += 1
    while change > 4:
        change -= 5
        nickels += 1
    while change > 0:
        change -= 1
        pennies += 1

    return quarters, dimes, nickels, pennies