
#Below is my solution
n=1
sum=0 
 
while(1):
	c=0
	if(n==1000): break
	if((n%3)==0): 
		sum+=n
		c=1;
	if(((n%5)==0) and (c==0)):sum+=n
	n=n+1

print("Total sum for the multiples of 3 & 5 lessthan", n ,"is", sum)


