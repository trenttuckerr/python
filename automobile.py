'''
Created on Nov 17, 2021

@author: trenttucker
'''
from test.test_importlib.test_abc import make_abc_subclasses
from pyexpat import model
from Restaurant import prices

class Automobile:
    def  __init__(self, make, model, price, milage):
        self.__make = make
        self.__model = model
        self.__price = price
        self.__milage = milage

    # setter methods
    def set_make(self, m):
        self.__make = m
        
    def set_model(self, m):
        self.__model = m
        
    def set_price(self, p):
        self.__price = p
        
    def set_milage(self, m):
        self.__milage = m
   
    # getter methods    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_price(self):
        return self.__price
    
    def get_milage(self):
        return self.__milage
        
class Car(Automobile):
    def __init__(self, make, model, price, milage, doors):
        Automobile.__init__(self, make, model, price, milage)
        self.__doors = doors
        
    def set_doors(self, doors):
        self.__doors = doors
        
    def get_doors(self):
        return self.__doors    
    
class Truck(Automobile):
    def __init__(self, make, model, price, milage, drive_type):
        Automobile.__init__(self, make, model, price, milage)
        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type
        
    def get_drive_type(self):
        return self.__drive_type
    
class Suv(Automobile):
    def __init__(self, make, model, price, milage, pass_cap):
        Automobile.__init__(self, make, model, price, milage)
        self.__pass_cap = pass_cap
        
    def set_passenger_capacity(self, pass_cap):
        self.__pass_cap = pass_cap
        
    def get_passenger_capacity(self):
        return self.__pass_cap
        
def main():
    make = input('enter car make')
    model = input('enter car model')
    price = input('enter car price')
    milage = input('enter car milage')
    doors = input('enter car doors')
    car = Car(make, model, price, milage, doors)
    print(car.get_make())
    print(car.get_model())
    print(car.get_price())
    print(car.get_milage())
    
    
    