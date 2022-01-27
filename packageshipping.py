'''
Created on Sep 18, 2021

@author: Trent Tucker
'''

# hw 3

# question 1, software packages

# prompt user for package to purchase number
packages = int(input('enter the number of packages purchased'))
discount = 0
total = 0.0
# run through different ranges to find discount
if(packages >= 10 and packages <= 19):
    discount = 10
elif(packages >= 20 and packages <= 49):
    discount = 20
elif(packages >= 50 and packages <= 99):
    discount = 30
elif(packages >= 100):
    discount = 40
# display discount amount and total after discount
print('the discount is', discount, '% and the total is ', end = '')
# divide discount by 100 for total calculation
discount /= 100
total = packages * 99
total_with_discount = total - total * discount
print('$', total_with_discount)

# question 2, Fast Freight

# prompt user for weight
weight = float(input('enter the weight of the package'))
rate = 0.0
shipping_charges = 0.0
# run through different ranges to find rate per pound
if(weight <= 2.0):
    rate = 1.50
elif(weight > 2.0 and weight <= 6.0):
    rate = 3.00
elif(weight > 6.0 and weight <= 10.0):
    rate = 4.00
elif(weight > 10.0):
    rate = 4.75
# calculate shipping charges
shipping_charges = weight * rate
# display result
print('shipping charges are $', shipping_charges)

# question 3, dates

# prompt user for month (in numeric form), day, and two-digit year
month = int(input('enter a month in numeric form'))
day = int(input('enter a day of the month'))
year = int(input('enter a two-digit year'))
# determine if month times day equals the year, and tell if it's magic
if(month*day == year):
    print('date is magic')
else:
    print('date is not magic')

# challenge question

seconds = int(input('enter a number of seconds'))
days = 0
hours = 0
minutes = 0

# time is minutes and seconds
if(seconds >= 60 and seconds < 3600):
    minutes = seconds // 60
    seconds = seconds - (60 * minutes)
    print(minutes, ':', seconds)
    
# time is hours, minutes, and seconds
elif(seconds >= 3600 and seconds < 86400):
    hours = seconds//3600
    seconds = seconds - hours * 3600
    minutes = (seconds - (3600 * hours)) // 60
    seconds = seconds - minutes * 60
    print(hours, ':', minutes, ':', seconds)

# time is in days, hours, minutes, and seconds
elif(seconds >= 86400):
    days = seconds // 86400
    seconds = seconds - 86400 * days
    hours = seconds // 3600
    seconds = seconds - hours * 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60    
    print(days, ':', hours, ':', minutes, ':', seconds)