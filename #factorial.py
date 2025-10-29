#factorial
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#import math function
import math
print(math.factorial(5))

#factorial using functions
def factorial(n):
    if n==0 or n==1:
        return 1
    fact=1
    for i in range(2,n+1):
        fact*=i
print(fact)
