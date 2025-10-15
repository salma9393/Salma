
#program to check sum of 2 numbers is even or odd:
a,b=map(int,input("enter the value:").split())
if(a+b)%2==0:
  print("even sum")
else:
  print("odd sum")

a=10
b=20
if (a+b)%2==0:
  print("even sum")
else:
  print("odd sum")

#program to find type of the triangle based on sides
a,b,c=map(int, input("enter the value:").split())
if (a==b==c):
  print("equilateral traingle")
elif(a==b or b==c or c==a):
  print("isosceles traingle")
else:
  print("scelene traingle")

#program to check if a number is given range
num=2
if num>=1 and num<=10:
  print("with in the range")
else:
  print("out of the range")

# program to check if a year is century year
year=2009
if(year%100==0):
  print("century year")
else:
  print("not a century year")

#program to sum of even numbers  in a range (while using loop)
num=6
sum=0
while (num>0):
  if (num%2==0):
    sum=sum+num
    num=num-1
print(num)