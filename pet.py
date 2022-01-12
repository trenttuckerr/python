'''
Created on Nov 15, 2021

@author: trenttucker
'''

class Pet:
    def  __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0

    def set_name(self, n):
        self.__name = n
        
    def set_animal_type(self, a):
        self.__animal_type = a
        
    def set_age(self, ag):
        self.__age = ag
        
    def get_name(self):
        return self.__name
        
    def get_animal_type(self):
        return self.__animal_type
        
    def get_age(self):
        return self.__age
    
def main():
    p = Pet()
    name = input('enter pet name')
    animal_type = input('enter pet type')
    age = input('enter pet age')
    p.set_name(name)
    p.set_animal_type(animal_type)
    p.set_age(age)
    print('the pet name is', p.get_name())
    print('the pet type is', p.get_animal_type())
    print('the pet age is', p.get_age())
    
main()