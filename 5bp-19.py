
#left triangle pattern of the multiplication table
num=1
for i in range(1,6):
  for j in range(num,num+i):
    print(2*j, end=" ")
  print()

#cyclic right shift of list
ls=[1,2,3,4,5]
k=2
print(ls[-k:]+ls[:-k])

# replace everyword in a list that contain'a' to @
ls=["word","apple","hello","cat","rat"]
print(list(map(lambda x:x.replace('a','@'),ls)))

#find the fibonacci series
#0,1,2,3...
n1,n2=0,1
n=1
while n<=10:
  print(n1,end=" ")
  next=n1+n2
  n1=n2
  n2=next
  n+=1

#alphabet pattern
import string
a=list(string.ascii_uppercase)
index=0
for i in range(1,26):
  for j in range(i):
    if index<len(a):
      print(a[index],end="")
      index+=1
print()

