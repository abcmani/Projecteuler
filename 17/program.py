"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

import time as T
start=T.time()
import math as M

target=1000

a=['one','two','three','four','five','six','seven','eight','nine','ten']
b=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
c=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
num_and=3 #and
num_hundred=7 #hundred
count=11 #thousand 

ones,tws,tens,doubldgt=dict(),dict(),dict(),dict()
ones.update({0:0})
tens.update({0:0})
for j in range(1,len(a)+1):
    ones[j]=len(list(a[j-1]))
print(ones)

i=0
for j in range(11,10+len(b)+1):
    tws[j]=len(list(b[i]))
    i+=1
print(tws)

i=0
for j in range(10,100,10):
    tens[j]=(len(list(c[i])))
    i+=1
print(tens)

doubldgt.update(ones)
doubldgt.update(tws)
print(doubldgt)

def getcount(n):
    #print(n)
    if(n/10 <1):
        return ones[n%10]
    elif n/100 < 1:
        if n <= 20  and n>10:
            return tws[n]
        elif n%10==0:               #handling 10,20,30,40..
            return tens[n]
        else:
            return tens[int(n/10)*10]+ones[n%10]
    if n%100==0 and n/100>=1:           #handling 100,200,300,...
        return ones[int(n/100)]+num_hundred
    elif n%100<=20:
        return ones[int(n/100)]+num_hundred+num_and+doubldgt[n%100]
    else:
        return ones[int(n/100)]+num_hundred+tens[int((n%100)/10)*10]+num_and+ones[n%10]

for i in range(1,target):
    count+=getcount(i)

#print(ones,'\n',tws,'\n',tens)
print("The sum of letters of numbers from 1 to 1000 is: ",count)
print("executed in ",T.time()-start,"Seconds")

'''============OUTPUT============
The sum of letters of numbers from 1 to 1000 is:  21124
executed in  0.062400102615356445 Seconds
=============================='''

