# printing a fibanacii series///

a,b=0,1
temp=0
sum=0
target=4000000
while(1):
	temp=a+b
	a=b
	b=temp
	if(temp>target):
		break
	print("Fibanacci number: ",temp)
	if(temp%2==0):
		sum=sum+temp
print('sum of even fibanacci numbers till ',target,'is : ',sum)