
#program for armstrong or not
num=153
length=len(str(num))
temp=num
sum=0
while temp!=0:
  rem=temp%10
  sum=sum+rem**length
  temp=temp//10
if sum==num:
    print("armstrong")
else:
    print("not an armstrong")

#prime number
def prime(num):
  if num>1:
    for j in range(2,num):
      if num%j==0:
        break
    else:
      print(num)
for i in range(2,10):
        prime(i)

#prime number or not
n=35
if n>1:
  for i in range (2,n):
    if n%i==0:
      print("not a prime")
      break
  else:
    print("prime number")

#area of circle
r=6
pi=3.14
area=pi*(r**2)
print("area of circle is ",area)

#sum of squares of n natural numbers
n=4
sum=((n*(n+1)*(2*n+1))//6)
print(sum)