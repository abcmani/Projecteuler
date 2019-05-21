#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?


def isPrime(target):
    count=0
    for i in range(1,int(math.sqrt(target))+1):                         #for i in range(1,target+1):
        if(target%i==0): count+=1
    return 1 if(count==1) else 0                            #count==2


#print(isPrime(7))

import time
import math
start=time.time()
i,a,target=2,list(),10001
while(1):
    if(len(a)==target):
        break
    if(isPrime(i)):
        a.append(i)
        print(len(a),"th Prime: ",i)
    i+=1
print("Found ",target," th prime: " ,max(a))
print("Executed in ",time.time()-start," Seconds")

"""================OUTPUT==============
10001 th Prime:  104743
Found  10001  th prime:  104743
Executed in  96.18950176239014  Seconds
====================================

================OUTPUT==============
Found  10001  th prime:  104743
Executed in  1317.4703550338745  Seconds
===================================="""
