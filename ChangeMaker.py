'''
Created on Oct 3, 2022

Program that returns
the correct number of change of quarters, dimes, nickels, and pennies
when given an integer between 0 to 99 provided from a user's input.

@author: Brian Trickovic
'''
originalAmount = 0

print('Please enter your amount as an integer between 0 and 99:')

# checks and ensures the user is inputting
# the correct type (integer) and a number that is in a range of 0 to 99
# then assigns the inputted value when conditions are met
while True:
    try:
        originalAmount = int(input())
    except ValueError:
        print('Please enter an integer:')
        continue
    if originalAmount >= 0 and originalAmount <= 99:
        print(f'{originalAmount}')
        break
    else:
        print('Your amount must be an integer between 0 and 99:')

# Keeps track of difference after each subtraction occurs
amount = originalAmount

# Obtains the number of quarter coins then subtracts the amount by the face value of those coins
quarters = amount // 25
amount = amount - (25 * quarters) 

# Obtains the number of dime coins from the difference then subtracts the amount by the face value of those coins
dimes = amount // 10
amount = amount - (10 * dimes)

# Obtains the number of nickel coins from the new difference then subtracts the amount by the face value of those coins
nickels = amount // 5
amount = amount - (5 * nickels)

# The amount that is left after all quarters, dimes, and nickels are taken away will always be less than 5, whereby the face value is equivalent to the number of coins of a penny
pennies = amount

# Prints the results into the console
print('Your change for your amount', originalAmount, 'is:')
print(quarters, 'quarters')
print(dimes, 'dimes')
print(nickels, 'nickels')
print(pennies, 'pennies')