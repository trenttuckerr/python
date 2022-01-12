'''
Created on Nov 17, 2021

@author: Trent Tucker
'''

def main():
    # retrieve string from user
    s = input('enter string for shuffling')
    # initialize the list which will hold integer indices
    indices = []
    # run for loop to get values for indices list
    # loop is structured to ensure amount of values
    # appended to the list is the same as the length of string
    for _ in range(len(s)):
        num = int(input('enter integer for indices list'))
        indices.append(num)
    # call shuffle method for s and indices
    print(shuffle(s, indices))
    
def shuffle(shuffle, ind):
    # initialize result which will store the shuffled string
    result = ''
    # iterate through the ind list
    for i in ind:
        # add the character at the specified index in the list
        # to the result string
        result += shuffle[i]
    return result
    
main()