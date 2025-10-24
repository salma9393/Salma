#prime or not
num=5
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not a prime")
            break
    else:
        print("prime")


#prime  or not
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
print(is_prime(5))  

#using lambda function
num=5
is_prime =lambda num: num>1 and all( num%i==0 for i in range(2,num))
print(is_prime)

