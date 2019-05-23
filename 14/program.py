"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
"""
import time as T
start_time=T.time()

def get_nxt_num(n):return int(n/2) if(n%2==0) else 3*n+1

start=1000000
#chain=list()
chain=0
temp=start
next_num=0
largest_chain,num_large_chain=0,0
while(1):
    if(next_num==1):
        #print("chain : ",chain)
        #if(len(chain)>largest_chain):
        if(chain>largest_chain):
            #largest_chain=len(chain)
            largest_chain=chain
            num_large_chain=start
        #chain=list()
        chain=0
        next_num=0
        temp=start-1
        start-=1
    if(start==1): break
    if(next_num==0):
        next_num=get_nxt_num(temp) 
    else:
        next_num=get_nxt_num(next_num)
    #chain.append(next_num)
    chain+=1
    #print(chain)
    temp-=1
    


#print(get_nxt_num(13))
print(num_large_chain," number has longest chain of length ",largest_chain)
print("Executed in ",T.time()-start_time," seconds")    """

"""
Improvement done in memory by not storing the chain values.,
even though execution is taking same time.
======= RESTART: C:/Users/vemulam/Desktop/Project Euler/14/program.py =======
837799  number has longest chain of length  524
Executed in  154.5734555721283  seconds
"""
"""=================Tried for Improved================"""

import time as T
start_time=T.time()

def get_nxt_num(n):return int(n/2) if(n%2==0) else 3*n+1

start=3
chain=0

largest_chain,num_large_chain=0,0
temp=start
while(start!=1):
    
    if(temp==1):
        #print("chain : ",chain)
        if(chain>largest_chain):
            largest_chain=chain
            num_large_chain=start
        chain=0
        temp=start-1
        start-=1
    if(temp%2==0):
       chain+=1
       temp=int(temp/2)
    else:
        chain+=2
        temp=int((temp*3+1)/2)
    print("Chain",chain)
    temp-=1
    print("Temp",temp)
    


#print(get_nxt_num(13))
print(num_large_chain," number has longest chain of length ",largest_chain)
print("Executed in ",T.time()-start_time," seconds")    
