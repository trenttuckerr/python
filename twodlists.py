'''
Created on Nov 1, 2021

@author: trenttucker
'''
from posix import times

# main method used to run all questions
def main():
    string_to_digit()
    list_2d()
    majority()
    vowels_and_consonants()
    
def string_to_digit():
    # create a list that will be added to
    user_list = []
    # run retrieval loop for as long as user wants (using cont)
    cont = 1
    while(cont == 1):
        # prompt user for entries to add to list
        to_add = input('enter a string to add to your list')
        user_list.append(to_add)
        # modify cont based off user wishes
        cont = int(input('add another value? 0 -> no, 1 -> yes'))
    # part a 
    # create string that will hold all numbers one after another
    to_convert = ""
    # run through list and add each element to to_convert
    for i in user_list:
        to_convert += i
    # we now have all the elements, back to back, as a single string
    # convert this string to an int using simple conversion functions
    to_convert = int(to_convert)
    # part b
    # reverse the order of the values in original list
    user_list.reverse()
    # repeat part a, but store result in new variable (same logic)
    to_convert2 = ""
    for i in user_list:
        to_convert2 += i
    to_convert2 = int(to_convert2)
    # part c
    # check for equality between two integers, print correct statement
    if(to_convert == to_convert2):
        print("number from list is palindromic")
    else:
        print('number from list is not palindromic')
    
def list_2d():
    # 2d lists
    # retrieve desired rows and columns from user
    rows = int(input('enter rows'))
    cols = int(input('enter cols'))
    # initialize he user's list
    user_list = []
    # run a nested loop, starting the outer running till cols
    for _ in range(0, cols):
        temp = []
        # inner runs till rows
        for __ in range(0 , rows):
            # retrieve user desired value
            val = int(input('enter value to enter to 2d list'))
            # utilize the temporary list to append val
            temp.append(val)
        # append the temporary list to the user_list
        user_list.append(temp)
    print('your created list is:', user_list)
    # finding the sum of all the values
    sum_list = 0
    # use same nested for loop methodology to iterate through 2d list
    for i in range(0, cols):
        for j in range(0, rows):
            # add the current element dictated by i and j values to the sum variable
            sum_list += user_list[i][j]
    print('the sum of all the values in the 2d list is', sum_list)
    # finding the product of all the values in the 2d list
    # initialize product_list to 1 to avoid multiplying by 0
    product_list = 1
    # use same nested for loop methodology to iterate through 2d list
    for i in range(0, cols):
        for j in range(0, rows):
            # calculate product and add it to the product variable
            product_list *= user_list[i][j]
    print('the product of all the values in the 2d list is', product_list)
        
def majority():
    # create nums, which will be added to by the user
    nums = []
    # used to track if user wants to keep adding to nums
    cont = 1
    while(cont == 1):
        to_add = int(input('enter num to add to nums (BEFORE STOPPING THERE MUST BE A MAJORITY ELEMENT)'))
        # add the element to nums
        nums.append(to_add)
        cont = int(input('keep adding? 0 -> no, 1 -> yes'))
    print('the list used for this run is', nums)
    # initialize max_occurrences which keeps the max occurrences of any one number in nums
    max_occurrences = 0
    # keeps track of the majority element
    majority = 0
    for i in nums:
        # temporary occurrence tracker for i
        times = 0
        # run a nested loop since we must iterate through the original list for an element
        for j in nums:
            if(i == j):
                # if we get here, it means there was an occurrence of i
                times += 1
        # check if times is greater than max_occurrences and if it appears more than floor times
        if(times > max_occurrences and times > (len(nums)//2)):
            # change max_occurrences to times, and change the majority element to i
            max_occurrences = times
            majority = i
    print('the majority element is', majority, 'and it appears', max_occurrences, 'times')

def vowels_and_consonants():
    # create the alphabet list
    alphabet = []
    # used to track if user wants to keep adding to nums
    cont = 1
    while(cont == 1):
        to_add = input('enter a letter to add to your alphabet')
        # add the element to alphabet
        alphabet.append(to_add)
        cont = int(input('keep adding? 0 -> no, 1 -> yes'))
    # create the vowel list, used for checking if in (and not in) alphabet
    vowels = ['a', 'e', 'i', 'o', 'u']
    # create count variables for vowels and consonants
    v_count = 0
    c_count = 0
    # run through the alphabet string
    for i in alphabet:
        # check if current element is a vowel
        if(i in vowels):
            # increment the vowel count
            v_count += 1
        else:
            # increment the consonant count since the letter is not a vowel
            c_count += 1
    print('in your alphabet there are', v_count, 'vowel(s) and', c_count, 'consonant(s)')
    
main()