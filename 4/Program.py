#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import time
start_time=time.time()
def palindrome(target):

        temp,s = target,0
        while(target>0):
                rem=target%10
                s=s*10+rem
                target=int(target/10)
        if(temp==s):
                print("Largest palindrome number from product of two 3 digits found")
                print("Paindrome number: ",temp)
                return 1
        else:
                return 0
        
#palindrome(121)

num1,num2=999,999

while(1):
      if(num1>=num2):       #Removing the reverse checks (a*b is same as b*a)
              #print("Both numbers:",num1,":",num2)
              if(palindrome(num1*num2)):break
      if((num2-1)>=num1-100):
              num2=num2-1
      if(num2==num1-100):
              num1=num1-1
              num2=999
print("Palindrome found with numbers ",num1,",",num2," in ",time.time()-start_time," Seconds")

"""----------------------Old version----------------------------------

import time
start_time=time.time()
def palindrome(target):

        temp,s = target,0
        while(target>0):
                rem=target%10
                s=s*10+rem
                target=int(target/10)
        if(temp==s):
                print("Largest palindrome number from product of two 3 digits found")
                print("Paindrome number: ",temp)
                return 1
        else:
                return 0
        
#palindrome(121)

num1,num2=999,999

while(not (palindrome(num1*num2))):
        
      if((num2-1)>=num1-100):
              num2=num2-1
      if(num2==num1-100):
              num1=num1-1
              num2=999
print("Palindrome found with numbers ",num1,",",num2," in ",time.time()-start_time," Seconds")"""
