#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#=================improved version====================
import sys
import time
import math
start_time=time.time()
temp=target=600851475143#int(sys.maxsize/16)
a=list()
for i in range(2,int(target+1)):
	count=0
	if(i>math.sqrt(temp)):break
	if(target%i==0):
		for j in range(2,i+1):
			if(i%j==0):
				count+=1
		if(count==1):
			a.append(i)
			target/=max(a)
			

print("Prime Factors of ",temp,' are:',a)
print('Executed in ',(time.time()-start_time),' seconds')

#======================================================


"""target=600851475143
a=list()
prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
if(target)
for i in range(2,target+1):
	count=0
	if(target%i==0):
		for j in range(2,i+1):
			if(i%j==0):
				count+=1
		if(count==1):
			a.append(i)

print("Factors of ",target,' are:',a)"""