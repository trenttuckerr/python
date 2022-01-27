'''
Created on Sep 22, 2021

@author: Trent Tucker
'''
# lab 5

# retrieve input for running of the program
n = int(input('enter a positive integer to enter the Collatz Sequence'))

# print the initial value to start showing the sequence of calculations
print(n, "-> ", end = '')

# ensure input is a positive integer
while(n < 1):
    n = int(input('enter a positive integer to enter the Collatz Sequence'))
    
# run while the number is not one, as that is when we end the sequence
while(n != 1):
    # check if the number is even
    if(n % 2 == 0):
        # perform proper calculation
        n //= 2
    # since we have verified input and checked if it was even
    # we can use a simple else since n would have to be odd
    else:
        # perform proper calculation
        n = 3 * n + 1
        
    # only print with arrow when n isn't one    
    if(n != 1):
        print(n, '-> ', end = '')
        
# print n, which is one at the end
print(n)
