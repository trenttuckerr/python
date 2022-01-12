'''
Created on Nov 17, 2021

@author: trenttucker
'''

class Car:
    def  __init__(self, y, m):
        self.__year_model = y
        self.__make = m
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        
    def brake(self):
        self.__speed -= 5
        
    def get_speed(self):
        return self.__speed
    
    
def main():
    c = Car(1990, 'Ford Mustang')
    for _ in range(5):
        c.accelerate()
        print('current speed:', c.get_speed())
    for _ in range(5):
        c.brake()
        print('current speed:', c.get_speed())
    
    
main()