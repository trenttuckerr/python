'''
Created on Oct 6, 2021

@author: Trent Tucker
'''
# declare math import so factorial can be used
import math
# --------------------------------------------
# number 1 of hw
x = int(input('enter x'))
n = int(input('enter n'))
# store sum for this question (start at 1 since series
# adds 1 in the beginning)
sum_1 = 1
# run loop to n+1 so i can become n
for i in range(1, n+1):
    sum_1 += (x**i)/(math.factorial(i))
# print sum for this question
print('sum for number 1 is', sum_1)
# --------------------------------------------

# number 2 of hw
# collect input
x = int(input('enter x for 2'))
n = int(input('enter n for 2'))
# store the sum for this problem
sum_2 = 0
# run all the way from 1 to n (where i becomes n)
for i in range(1, n + 1):
    # add used equation to the sum
    sum_2 += (x**i)/i
# output the sum
print('sum for number 2 is', sum_2)
# --------------------------------------------

# number 3 of hw
n = int(input('enter n for 3'))
# store the sum for this problem
sum_3  = 0
# this sequence cubes number and starts at 1
num = 1
while(num <= n):
    # cube start and add to sum
    sum_3 += num**3
    # increment num to run through numbers
    num += 1
# output the sum
print('sum for number 3 is', sum_3)
# --------------------------------------------

# number 4 of hw
# retrieve user input
n = int(input('enter n for 4'))
# store sum for this problem
sum_4 = 0
# start at 1 so create variable
num = 1
while(num <= n):
    # take factorial of num and add it to sum
    sum_4 += math.factorial(num)
    # increment num to run through numbers
    num += 1
# print the sum for this problem
print('sum for number 4 is', sum_4)
# --------------------------------------------