#factorial of a numbers
num=5
fact=1
while num>=1:
    fact=fact*num
    num=num-1
print(fact)


num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)




import math
print(math.factorial(5))





from math import factorial
print(factorial(5))