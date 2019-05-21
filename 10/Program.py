'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million(2000000).'''


import time as T
start=T.time()
import math

def isPrime(target):
    count=0
    for i in range(1,int(math.sqrt(target))+1):                         #for i in range(1,target+1):
        if(target%i==0): count+=1
    return 1 if(count==1) else 0                            #count==2


#print(isPrime(7))




i,a,target=2,list(),2000000
while(1):
    if((i>2 and i%2==0) or (i>3 and i%3==0)or i%5==0):
        i+=1
        continue
    if(i>target+1):
        break
    if(isPrime(i)):
        a.append(i)
        #print(len(a),"th Prime: ",i)
    i+=1
#print("Found ",target," th prime: " ,max(a))
print("Sum of primes till ",target,"is: ",sum(a))
print("Executed in ",T.time()-start," Seconds")

'''========OUTPUT===============
Sum of primes till  2000000 is:  142913828917
Executed in  88.5680000782013  Seconds
==============================
#with elimination of even and multiples of 3
Sum of primes till  2000000 is:  142913828922
Executed in  109.22901725769043  Seconds
================================
#with even elimination
Sum of primes till  2000000 is:  142913828922
Executed in  163.6753659248352  Seconds
================================
#without print
Sum of primes till  2000000 is:  142913828922
Executed in  333.2483263015747  Seconds
========OUTPUT===============
148932 th Prime:  1999979
148933 th Prime:  1999993
Sum of primes till  2000000 is:  142913828922
Executed in  1557.5020840168  Seconds
============================='''
