#The sum of the squares of the first ten natural numbers is,

#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import time
start=time.time()
s=0
for i in range(1,101):
    s=s+i**2
print("The difference of squares sum and sum squares till 100 is", int(((100*(101/2))**2)-s),"Executed in ",time.time()-start," Seconds")

"""==============OUTPUT===========
The difference of squares sum and sum squares till 100 is 25164150 Executed in  0.0  Seconds
================================"""
