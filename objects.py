'''
Created on Nov 23, 2021

@author: trenttucker
'''
import random

def main():
    capital_quiz()
    frequency()
    # create three RetailITem objects
    item1 = RetailItem('Jacket', 12, 59.95)
    item2 = RetailItem('Designer Jeans', 40, 34.95)
    item3 = RetailItem('Shirt', 20, 24.95)
    # print the created objects
    print('item 1:', item1.get_desc(), item1.get_units(), item1.get_price())
    print('item 2:', item2.get_desc(), item2.get_units(), item2.get_price())
    print('item 3:', item3.get_desc(), item3.get_units(), item3.get_price())
    print('-----------------------------------')
    # create a sample patient
    sample_patient = Patient('John Michael Smith', '123 Apple St, Austin, TX, 78704', 
                             '(123)456-7890', 'Anna Marie Smith; (098)765-4321')
    # create procedure objects
    proc1 = Procedure('John Michael Smith', '123 Apple St, Austin, TX, 78704', 
                      '(123)456-7890', 'Anna Marie Smith; (098)765-4321', 'Physical exam',
                      'Nov. 20, 2021', 'Dr. Irvine', '250.00')
    proc2 = Procedure('John Michael Smith', '123 Apple St, Austin, TX, 78704', 
                      '(123)456-7890', 'Anna Marie Smith; (098)765-4321', 'X-ray',
                      'Nov. 20, 2021', 'Dr. Jamison', '500.00')
    proc3 = Procedure('John Michael Smith', '123 Apple St, Austin, TX, 78704', 
                      '(123)456-7890', 'Anna Marie Smith; (098)765-4321', 'Blood test',
                      'Nov. 20, 2021', 'Dr. Smith', '200.00')
    # display patient's info
    print(sample_patient.get_full_name(), sample_patient.get_address(),
          sample_patient.get_number(), sample_patient.get_emerg_contact())
    # display all three procedures
    print(proc1.get_name(), proc1.get_date(), proc1.get_pract(), proc1.get_charges())
    print(proc2.get_name(), proc2.get_date(), proc2.get_pract(), proc2.get_charges())
    print(proc3.get_name(), proc3.get_date(), proc3.get_pract(), proc3.get_charges())
    # display total charge
    print('Total charge:', float(proc1.get_charges()) + float(proc2.get_charges()) + float(proc3.get_charges()))
    
def capital_quiz():
    # initialize a dictionary with all states & corresponding capitals
    states_caps = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
    }
    # store user's choice to continue playing
    choice = ''
    ready = input('Ready to play states/capitals (y/n)?')
    # if ready, get to game, if not, break
    if(ready == 'y'):
        pass
    else:
        choice = 'n'
    correct = 0
    incorrect = 0
    while(choice != 'n'):
        # retrieve a random state by using choice method & random on a list conversion
        state = random.choice(list(states_caps.keys()))
        print('What is the captial of', state, '(use proper capitalization)?')
        guess = input('')
        if(guess == states_caps[state]):
            # increment the correct variable since answer was right
            correct += 1
            print('Correct! Want to play again (y/n)?')
            choice = input('')
        else:
            # increment the incorrect variable since answer was wrong
            incorrect += 1
            print('Incorrect. Want to play again (y/n)?')
            choice = input('')
    # when the user is done, print the number of correct and incorrect responses
    print('Game over. You answered', correct, 'question(s) correctly.')
    print('You answered', incorrect, 'question(s) incorrectly.')
    print('-----------------------------------')

def frequency():
    # open words for reading
    w = open(r'/Users/trenttucker/documents/words.txt', 'r')
    line = w.readline()
    line = line.rstrip("\n")
    # initlialize list which will hold all of the words in the file
    words_list = []
    # run until end of file
    while(line != ''):
        # add the word to the list, redefine line to next word
        words_list.append(line)
        line = w.readline()
        line = line.rstrip("\n")
    w.close()
    print(words_list)
    # initialize a list that will store already iterated words
    distinct_words = []
    for i in words_list:
        if(i not in distinct_words):
            # add i to done, which will give us distinct words
            distinct_words.append(i) 
    words_times = {}
    # iterate over the distinct words, utilize original words list,
    # and create the dictionary with words/frequency
    for i in distinct_words:
        occurrences = 0
        # run through words list for i in distinct words
        for j in range(len(words_list)):
            if(i == words_list[j]):
                occurrences += 1
        # add word and its frequency to dicitonary
        words_times[i]=occurrences
    # open a new file to write words and their frequency
    wf = open(r'/Users/trenttucker/documents/words_frequencies.txt', 'w')
    # display frequency of each word
    for key, value in words_times.items():
        print('The word', key, 'occurs', value, 'time(s).')
        # write the key and value to file
        wf.write(key)
        wf.write(' : ')
        wf.write(str(value))
        wf.write(' times \n')
    wf.close()
    print('-----------------------------------')
    
    
class RetailItem:
    def  __init__(self, desc, units, price):
        self.__desc = desc
        self.__units = units
        self.__price = price        

    def get_desc(self):
        return self.__desc
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price
    
class Patient:
    def __init__(self, full_name, address, number, emerg_contact):
        self.__full_name = full_name
        self.__address = address
        self.__number = number
        self.__emerg_contact = emerg_contact
        
    # accessor methods
    def get_full_name(self):
        return self.__full_name
    
    def get_address(self):
        return self.__address
    
    def get_number(self):
        return self.__number
    
    def get_emerg_contact(self):
        return self.__emerg_contact
    
    # mutator methods
    def set_full_name(self, full_name):
        self.__full_name = full_name
        
    def set_address(self, address):
        self.__address = address
        
    def set_number(self, number):
        self.__number = number
        
    def set_emerg_contact(self, emerg_contact):
        self.__emerg_contact = emerg_contact
        
class Procedure(Patient):
    def __init__(self, full_name, address, number, emerg_contact, name, date, pract, charges):
        Patient.__init__(self, full_name, address, number, emerg_contact)
        self.__name = name
        self.__date = date
        self.__pract = pract
        self.__charges = charges
    
    # accessor methods
    def get_name(self):
        return self.__name
    
    def get_date(self):
        return self.__date
    
    def get_pract(self):
        return self.__pract
    
    def get_charges(self):
        return self.__charges
    
    # mutator methods
    def set_name(self, name):
        self.__name = name
        
    def set_date(self, date):
        self.__date = date
        
    def set_pract(self, pract):
        self.__pract = pract
        
    def set_charges(self, charges):
        self.__charges = charges
    
    
    
    
    # mutator methods
        
main()