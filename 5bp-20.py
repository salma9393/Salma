
#number pattern
num=1
for i in range(1,5):
  for j in range(i):
    print(num,end=" ")
    num+=1
  print()

#left triangle star pattern
for i in range(1,6):
  for j in range(1,i+1):
    print("*",end=" ")
  print()

#right angle traingle star pattern
n=5
for i in range(1,n+1):
  for j in range (n-i):
    print(" ",end=" ")
  for k in range(i):
    print("*",end=" ")
  print()

#inverted right traingle star pattern
n=5
for i in  range(n,0,-1):
  for j in range(n-i):
    print (" ", end=" ")
  for k in range(i):
    print("*",end=" ")
  print()

#pyramid pattern
n=5
for i in range (1,n+1):
  for j in range(n-i):
    print(" ",end=" ")
  for k in range(2*i-1):
      print("*",end=" ")
  print()