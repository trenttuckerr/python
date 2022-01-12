'''
Created on Nov 4, 2021

@author: trenttucker
'''
def main():
    print('your entered string is a palindrome:', is_palindrome())
    remove_vowels()
    remove_duplicates()
    most_occurrences()

def is_palindrome():
    # retrieve user input
    user_string = input('enter a string to check if palindrome:')
    # convert the string to lower case for proper functioning of method
    user_string = user_string.lower()
    # start at the end, go to beginning, move backwards one by one
    # this string slicing methodology to reverse the string
    if(user_string == user_string[::-1]):
        return True
    else:
        return False

def remove_vowels():
    # retrieve user input
    user_string = input('enter a string to remove vowels from:')
    # define a vowel list used in removing
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # run through user_string
    for i in user_string:
        # check if current char is vowel, if so remove it
        if(i in vowels):
            # take the current character and replace it
            # with a blank string
            user_string = user_string.replace(i, '')
    print('your new string is:', user_string)
    
def remove_duplicates():
    # retrieve user input
    user_input = input('enter string to remove duplicates from:')
    # convert to lower case for proper functioning of methods
    user_input = user_input.lower()
    # create a list to store result
    no_dup = []
    # iterate through the string
    for i in user_input:
        # check if the current character is not in no_dup,
        # if it isn't, this means we need to add it
        if(i not in no_dup):
            no_dup.append(i)
    # utilize the join function to convert the list to a string
    no_dup = ''.join(no_dup)
    print('the string with no duplicates is:', no_dup)

def most_occurrences():
    # retrieve user input
    s = input('enter a string to find the character that occurs the most:')
    # convert to lower case to allow for proper function of method
    s = s.lower()
    # initialize a variables to store the most common character and how many times
    most = ''
    times = 0
    # iterate through s
    for i in range(0, len(s)-1):
        # initialize count to count the occurrences of i in s
        count = 0
        for j in range(0, len(s)-1):
            if(s[j] == s[i]):
                count += 1
        # check if the count of this character is more than the current
        # most occurred character's
        if(count > times):
            # reassign the proper most occurrences number and most occurred character
            times = count
            most = s[i]
    print('the character that occurs most in the string is:', most)
        
main()