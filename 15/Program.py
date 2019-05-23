"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
""" 


import time as T
start=T.time()

m,n=20,20   # given matrix size


mat=[[0 for x in range(n+1)] for y in range(m+1)]

for i in range(1,m+1):
    mat[i][0]=1
    mat[0][i]=1

for i in range(1,m+1):
    for j in range(1,n+1):
        mat[i][j]=int(mat[i-1][j])+int(mat[i][j-1])

#print(mat)
print(mat[m][n])
print("Executed in ",T.time()-start," Seconds")


"""
Concept inspiration: https://www.youtube.com/watch?v=trIkPmwTSyA
Solved by dynamic programing usage
Can be improved by using combinations concept ncr=n!/(n-r)!r!
Can be solved by writing pascal's Triangle mth line and nth column
======= RESTART: C:/Users/vemulam/Desktop/Project Euler/15/Program.py =======
137846528820
Executed in  0.062399864196777344  Seconds
"""
import math as M
import time as T
start=T.time()
m,n=20,20
# maing the rows & columns in ncr format so ncr will be m+nCm
result=int(M.factorial(m+n)/(M.factorial(n)*M.factorial(m)))

print(result)
print("Executed in ",T.time()-start," Seconds")
"""
======= RESTART: C:/Users/vemulam/Desktop/Project Euler/15/Program.py =======
137846528820
Executed in  0.015599966049194336  Seconds
"""
