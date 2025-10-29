#gcd find
def gcd(a,b):
    while b:
        a=b
        b=a%b
    return a
print(gcd(16,12))

#gcd
import math
print(math.gcd(48,12))
