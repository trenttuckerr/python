'''
Created on Nov 17, 2021

@author: trenttucker
'''
from test.test_long import SHIFT
class Employee2:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
class Production_Worker(Employee2):
    def __init__(self, name, number, shift, rate):
        Employee2.__init__(self, name, number)
        self.__shift = shift
        self.__rate = rate
    
    def get_shift(self):
        return self.__shift
    
    def get_rate(self):
        return self.__rate
    
def main():
    name = input('enter name')
    number = input('enter number')
    shift = input('enter shift')
    rate = input('enter rate')
    prod_worker = Production_Worker(name, number, shift, rate)
    print('name is', prod_worker.get_name())
    print('number is', prod_worker.get_number())
    print('shift is', prod_worker.get_shift())
    print('rate is', prod_worker.get_rate())
    
main()
    
