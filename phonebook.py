'''
Created on Nov 10, 2021

@author: trenttucker
'''
def main():
    phoneBook()
    
def phoneBook():
    # initialize a dictionary for the phone book
    phBook = {'John':'938477566', 'Jack':'938377264', 'Jill':'947662781'}
    # utilize keys method and a for loop for printing names
    print('The names in the phone book are ', end = '')
    # keys method - returns the keys
    for keys in phBook.keys():
        print(keys, end = ' ')
    print()
    # utilize values method and a for loop for printing values
    print('The phone numbers in the phone book are ', end = '')
    # values method - returns sequence of values
    for vals in phBook.values():
        print(vals, end = ' ')
    print()
    # add Jake to existing dictionary
    phBook['Jake']='938273443'
    # remove Jill from existing dictionary
    del phBook['Jill']
    # print elements in dictionary using items method and for loop
    # loop over these tuples
    for key, value in phBook.items():
        print('The phone number of', key, 'is', value) 
    # set up try/except to catch the case where the user input is invalid for the name
    try:
        # retrieve user input to search for the value of key input
        user_key = input('Enter the name to find desired person\'s number: ')
        print(user_key + '\'s', 'number is', phBook[user_key])
    except:
        print('ERROR: The given name,', user_key + ',', 'does not exist in the phonebook')

main()