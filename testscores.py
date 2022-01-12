Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:19) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
'''
Created on Oct 14, 2021

@author: trenttucker
'''

import random

def main():
    # initialize array to store scores
    test_scores = []
    # retrieve the 5 test scores from user, and add them to array
    score_1 = float(input('enter first test score'))
    test_scores.append(score_1)
    score_2 = float(input('enter second test score'))
    test_scores.append(score_2)
    score_3 = float(input('enter third test score'))
    test_scores.append(score_3)
    score_4 = float(input('enter fourth test score'))
    test_scores.append(score_4)
    score_5 = float(input('enter fifth test score'))
    test_scores.append(score_5)
    # run through array to print test letters
    for i in range(1,5+1):
        print('score', i , ':', determine_grade(test_scores.pop(0)))

    # print the average
    print('average: ', calc_average(score_1, score_2, score_3, score_4, score_5))
    # ---------------------------------------------------------------------------
        
    # prompt user for number to determine if it's prime
    user_num = int(input('enter a number to determine if it is prime'))
    # send user_num to the prime function and store its return value
    prime = is_prime(user_num)
    # print whether the number is prime or not based off the return value
    if(prime):
        print(user_num, 'is prime')
    else:
        print(user_num, 'is not prime')
    # ---------------------------------------------------------------------------
    
    # call print_prime which will print all prime numbers 1 to 100
    print_prime()
    # ---------------------------------------------------------------------------
    
    # run the odd even counter
    odd_even_counter()
    # ---------------------------------------------------------------------------

def calc_average(s1, s2, s3, s4, s5):
    # compute and return average
    return((s1 + s2 + s3 + s4 + s5) / 5)
    
    
def determine_grade(score):
    # run through different ranges, return corresponding letter
    if(score >= 90):
        return('A')
    elif(score >= 80):
        return('B')
    elif(score >= 70):
        return('C')
    elif(score >= 60):
        return('D')
    else:
        return('F')
    
def is_prime(num):
    # reserve this to return false is 1 is sent (1 is not prime)
    if(num == 1):
        return False
    # run a for loop from 2 to the number to check for a factor
    for i in range(2, num):
        if(num % i == 0):
            # return false due to a factor being found
            return False
    # return true since it passed the for loop without returning
    return True

def print_prime():
    print('prime numbers 1 to 100:')
    # run a for loop 1 to 100 calling is_prime to determine
    # if number is prime (only print the prime ones)
    for i in range(1, 100 + 1):
        if(is_prime(i)):
            print(i, ' ', end = '')
    print('')

def odd_even_counter():
    # create variables to count even and odd occurrences
    even = 0
    odd = 0
    # run a for loop that will run 100 times
    for _ in range(1, 100 + 1):
        rand = random.randint(1, 10)
        # check if odd, add to count so
        if(rand % 2 != 0):
            odd += 1
        # must be even here
        else:
            even += 1
    # print the results
    print('after 100 random numbers were generated,', even, 'were even,', odd, 'were odd')

main()