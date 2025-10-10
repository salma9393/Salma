
#leap year or not
year=int(input("enter the year:"))
if year%400==0 and year%100==0:
  print("leap year")
elif year%4==0 and year%100!=0:
  print("leap year")
else:
  print("not a leap year")

#declare a variables in three ways
x=10
y=20
print(x)
print(y)

x,y=10,20
print(x,y)
print(y,x)

x=t=10
print(x)
print(t)

#square of a number
sr=7**2
print(sr)

#area of the traingle
b=float(input())
h=float(input())
area=(1/2)*b*h
print(area)

#swapping of values using four methods
x=10
y=20
temp=x
x=y
y=temp
print(x,y)

x=10
y=20
(x,y)=(y,x)
print(x,y)

x=10
y=20
y=x+y
x=y-x
y=y-x
print(x,y)

x=10
y=20
y=y-x
x=x+y
print(x,y)