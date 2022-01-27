'''
Created on Sep 1, 2021

@author: Trent Tucker
'''
# displaying welcome message
print("""Welcome. This program will help split a restaurant
bill between friends as well suggesting the percentage tip.""")

# taking user inputs for all variables
final_bill_amt = float(input("What is the final bill amount?"))
people = int(input("How many people are splitting the bill?"))

# internal calculation
final_15 = (final_bill_amt * .15) + final_bill_amt
final_20 = (final_bill_amt * .20) + final_bill_amt
each_final = final_bill_amt / people
each_15 = final_15 / people
each_20 = final_20 / people

# display final values on screen
print("Final Bill Amount = $", final_bill_amt)
print("Final Bill Amount + 15% tip = $", final_15)
print("Final Bill AMount + 20% tip = $", final_20)
print("Number of people splitting the bill = ", people)
print("Each person's share of the actual final bill without including the tip = $", each_final)
print("Each person's share with 15% tip included = $", each_15)
print("Each person's share with 20% tip included = $", each_20)