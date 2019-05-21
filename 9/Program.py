'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''


import time as T
start=T.time()
s=1000
a,b,c=3,4,5

while(1):
    if(a<b and b<c):
        if(a**2+b**2==c**2):
            print("Pythogarant triplents: ",a,",",b,",",c)
            if(a+b+c==s):break
    c+=1
    if(c==999):
        c=5
        b+=1
        if(b==999):
            c=5
            b=4
            a+=1
print("Product of only pythagarant triplet whose sum=1000 is: ",a*b*c," found in ",T.time()-start," seconds")
print("the triplests are:",a,",",b,",",c)

'''==============OUTPUT===========
Product of only pythagarant triplet whose sum=1000 is:  31875000  found in  201.74653911590576  seconds
the triplests are: 200 , 375 , 425
==============================='''
