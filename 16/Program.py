"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import time as T
import math as M
start=T.time()

sum=0
result=int(M.pow(2,1000))
result=list(str(result))
for i in result:
    sum=sum+int(i)
print(sum)
print("executed in ",T.time()-start,"seconds")

"""
======= RESTART: C:/Users/vemulam/Desktop/Project Euler/16/Program.py =======
1366
executed in  0.015599966049194336 seconds
"""
