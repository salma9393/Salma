#addition of two numbers values from user
a=int(input("enter 1st value:"))
b=int(input("enter 2nd value:"))
c=a+b
print(c)
print(a+b)

#maximum of two numbers using functions
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(20,30))

#factorial of a number
num=6
fact=1
for i in range (1,7):
    fact=fact*i
print(fact)

#simple interest program
p=18000
t=14
r=2
si=(p*t*r)/100
print(si)

p,t,r=18000,14,2
si=(p*t*r)/100
print(si)

#compound interest
p=18000
t=14
r=2
n=2
a=p*(1+r/n)**(n*t)
ci=a+p
print(ci)