'''
Created on Oct 6, 2021

@author: Trent Tucker

'''

# d(n) -> sum of proper divisors of n
# d(a) & d(b) (sums) are same, and a!=b -> amicable
# task: find all amicable numbers < 10000


# sum of a's divisors = x, if x's sum of divisors = a -> amicable


    
# find proper factors' sum, once find sum see if sum = initial num
# find d(a), store it
for a in range(1, 10000):
    # store da which is sum of factors of a
    da = 0 
    # find factors of a and add to da
    for j in range(1, a):
        if(a % j == 0):
            da += j
    # find factors of da, store that sum as db
    # set b equal to the sum of a's numbers
    b = da
    db = 0
    # now find the sum of b's numbers
    for k in range(1, da):
        if(da % k == 0):
            db += k
    # at this point we have found d(a)
    # and we have found d(b)
    # check if d(a) = b and d(b) = a (where a != b)
    if(da == b and db == a and a != b):
        print(a, ' ', da, end = ' ')