'''
Created on Nov 12, 2021

@author: trent tucker
'''

def main():
    # utilize try / except to check if menu file exists
    # if not, the error is caught and the menu file is created
    try:
        f = open(r'/Users/trenttucker/documents/menu.txt', 'r')
        # read the menu file to print the menu to the user
        menu_contents = f.read()
        f.close()

    # catch the OSError that is thrown when a file is not found,
    # and create the menu/add contents
    except OSError:
        f = open(r'/Users/trenttucker/documents/menu.txt', 'w')
        f.write('0. Exit the Order menu\n')
        f.write('1. Chicken Strips - $3.50\n')
        f.write('2. French Fries - $2.50\n')
        f.write('3. Hamburger - $4.00\n')
        f.write('4. Hotdog - $3.50\n')
        f.write('5. Large Drink - $1.75\n')
        f.write('6. Medium Drink - $1.50\n')
        f.write('7. Milk Shake - $2.25\n')
        f.write('8. Salad - $3.75\n')
        f.write('9. Small Drink - $1.25\n')
        f.close()
        # open the file in read mode to get the contents
        f = open(r'/Users/trenttucker/documents/menu.txt', 'r')
        # read the menu file to print the menu to the user
        menu_contents = f.read()
        f.close()
        
    # in the same fashion as the menu file, create and catch any
    # errors for the customer file
    try:
        s = open(r'/Users/trenttucker/documents/customers.txt', 'r')
        # initialize list to store lines which will help for printing
        lines = []
        # run until the end of the file (breaks when so)
        while(True):
            # read the line and strip the return new line sequence
            line = s.readline()
            line = line.rstrip("\n")
            # add the line to the list unless line is empty, in that case
            # it has reached the end of the file
            if(line != ''):
                lines.append(line)
            # break since end of file was detected
            else:
                break
        # if the file exists with no customers print this
        if(len(lines) == 0):
            print('This is the first customer of the day!')
        # otherwise print the previous customers order
        else:
            # retrieve and print the last line of the file which is last in the list
            print('Previous customer: ' + lines[len(lines)-1])    
        s.close()
        
    except OSError:
        s = open(r'/Users/trenttucker/documents/customers.txt', 'w')
        # there is no previous customer since the file had to be created,
        # so print the following message
        print('This is the first customer of the day!')
        s.close()
        
    # check if the user would like to order
    # begin a while loop that runs continuously, 
    # as code breaks within loop when user wishes
    while(True):
        print('Welcome to the restaurant!')
        
        # check to see if there is a customer
        # wanting to order
        print('Would you like to order?')
        print('(Yes -> y, No -> any other key)')
        to_order = input('')
        if(to_order == 'y'):
            # passing will move to the order taking
            pass
        else:
            # break since there's no order to be taken
            break
        
        print('Take a look at our menu.')
        print('When you are ready to order, please press 0.')
        print(menu_contents)
        # emulate a 'do while' loop that will run until
        # user is ready to order
        while(True):
            ready = input('')
            if ready != '0':
                print('Invalid input. Please press 0 when ready to order.')
            else:
                # break since the user is ready to order
                break
                
        print('What is the name for the order?')
        name = input('')
        print('Okay, great. What would you like to order, ' + name + '?')
        print('(Enter the number(s) of the item(s) off of the menu.)')
        # emulate another 'do while' loop that performs an error
        # check to make sure user did not enter 0 when ordering, as
        # well as other invalid character checks
        while(True):
            order = input('')
            # user find function which will be used to check if order contains
            # -1, if find does not return -1, a zero was found
            if(order.find('0') != -1):
                print('A zero was found in your order, which is not an item we sell.')
                print('Please re-enter your order (numbers 1-9).')
            # ensure order only contains 1-9
            else:
                # stores if the input is acceptable or not
                is_acceptable = True
                # initialize list of the numbers from the menu
                acceptable_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                # run loop to ensure every character of order is valid
                for i in order:
                    if(i not in acceptable_nums):
                        is_acceptable = False
                if(is_acceptable == False):
                    print('An invalid character was found in your order.')
                    print('Please re-enter your order (numbers 1-9).')      
                else:
                    # passes all catches, so it is valid input, get out of error check loop
                    break
        
        # convert the order which is a string into a list, so that
        # proper iteration and cost can be found for each item
        order_list = list(order)
        order_total = 0.0
        for i in order_list:
            order_total += prices(i)
        # format the total to two decimal points along with a leading
        # $
        order_total = "${:.2f}".format(order_total)
        print('Alright. This order\'s total is:', order_total)
              
        # open the customers file in append mode, as we will add to it
        s = open(r'/Users/trenttucker/documents/customers.txt', 'a')
        # use the name variable to write the current customer's name to the file 
        s.write(name + '; order included ')
        
        # run different for loops depending on the amount of items that 
        # the customer ordered, for formatting/grammar purposes
        
        # one item to add to file
        if(len(order_list) == 1):
            # code to add example: a milk shake. Price was (order_total)
            s.write(item_names(order_list[0]) + '. Price was ' + order_total + '.\n')
            s.close()
         
        # exactly 2 items to add to file    
        elif(len(order_list) == 2):
            # code to add example: milk shake and hot dog. Price was (order_total)
            s.write(item_names(order_list[0]) + ' and  ' + item_names(order_list[1]) +
                    '. Price was ' + order_total + '.\n')
            s.close()
                
        # more than 2 items to add to file    
        else:
            # code to add example: milk shake, hot dog, and large drink. Price was (order_total)    
            # run a for loop here for formatting purposes. on the last item, proper grammar
            # will be ensured for input to file
            for i in range(0, len(order_list)):
                # check if it is the last element in the list
                if(i == len(order_list) - 1):
                    # last item to add -> put in the and as well as price
                    s.write('and '  + item_names(order_list[i]) + '. Price was ' + order_total +
                            '.\n')
                    s.close()
                else:
                    # write the item with comma since there are more items to write
                    s.write(item_names(order_list[i]) + ', ')
        
    print('Thanks for choosing us. Have a good day!')
        
def prices(item):
    # define the menu as a dictionary with items/prices
    # items here is the number of food/drink
    menu = {'1' : 3.50,
            '2' : 2.50,
            '3' : 4.00,
            '4' : 3.50,
            '5' : 1.75,
            '6' : 1.50,
            '7' : 2.25,
            '8' : 3.75,
            '9' : 1.25}
    # return the price of the item
    return menu[item]
    
def item_names(num):
    #  define the menu as a dictionary with numbers/item names
    menu = {'1' : 'chicken strips',
            '2' : 'french fries',
            '3' : 'hamburger',
            '4' : 'hotdog',
            '5' : 'large drink',
            '6' : 'medium drink',
            '7' : 'milk shake',
            '8' : 'salad',
            '9' : 'small drink'}
    # return the name of the ordered item
    return menu[num]
        
main()