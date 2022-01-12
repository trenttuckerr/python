'''
Created on Oct 13, 2021

@author: trenttucker
'''
import random
# # open the file
# f = open("customers.txt", "w+")
# # write to the file
# f.write("John Smith\n")
# f.write("David Locke\n")
# # close it (done writing)
# f.close()
# # allow for reading
# f = open('customers.txt', 'r')
# # set variable to read it
# content = f.read()
# # print reading variable
# print(content)
# ----------------------------
f = open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'w')
f.write('John Smith\n')
f.write('David Locke\n')
f.close()

f = open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'a')
f.write('John Smith\n')
f.write('David Locke\n')
f.close()

f = open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'r')
file_contents = f.read()
f.close()
print(file_contents)

f = open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'r')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
f.close()
line1 = line1.rstrip("\n")
line2 = line2.rstrip("\n")
line3 = line3.rstrip("\n")
line4 = line4.rstrip("\n")
print(line1)
print(line2)
print(line3)
print(line4)

n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))
f = open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'w')
f.write(str(n1)+'\n')
f.write(str(n2)+'\n')
f.write(str(n3)+'\n')
f.close()

f = open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'r')
line1 = int(f.readline())
line2 = int(f.readline())
line3 = int(f.readline())
f.close()

number_days = int(input(''))
f=open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'w')
for i in range(1, number_days+1):
    sales = float(input(''))
    f.write(str(sales)+'\n')
f.close()

f=open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'r')
line=f.readline()
while line!='':
    amount=float(line)
    print(amount)
    line=f.readline()
f.close

f=open(r'C:\\Users\\trenttucker\\desktop\\customers.txt', 'r')
for line in f:
    amount = float(line)
    print(amount)
f.close()

# random number file writer
f=open(r'C:\\Users\\trenttucker\\desktop\\randoms.txt', 'w')
num_times = int(input('enter amount of ran nums to hold'))
n_sum = 0
for i in range (1, num_times+1):
    ran_num = random.randint(1, 500)
    n_sum += ran_num
    # note you must use str before when adding int/float
    f.write(str(ran_num)+'\n')
f.close()
f=open(r'C:\\Users\\trenttucker\\desktop\\randoms.txt', 'r')
# alt way to do it
# line=f.readline()
# count=0
# s=0
# while line!='':
#     count+=1
#     s+=int(line)
#     line=f.readline()
# average=s/count
randoms_content = f.read()
f.close()
print(randoms_content)
print('count of numbers is', num_times)
print('sum of numbers is', n_sum)
print('average of numbers is', n_sum/num_times)

    



