
#linearsearch
ls=[3,13,8,4,2]
t=13
index=-1
for i in range(len(ls)):
  if ls[i]==t:
    index=i
    break
print(index)

#binary search
ls=[1,2,3,4,5,6,7]
x=7
l,r,index =0,len(ls)-1,-1
while l<=r:
  mid=(l+r)//2
  if ls[mid]==x:
      index=mid
      break
  elif ls[mid]<x:
      l=mid+1
  else:
      r=mid-1
print(index)

#factors of a number
num=6
print("factors of a number:")
for i in range(1,num+1):
  if num%i==0:
    print(i)

#factorial of a number
num=4
fact=1
for i in range(1,num+1):
  fact=fact*i
print(fact)

#program for leap year
year=2030
if((year%4==0) and (year%100!=0)):
  print("leap year")
else:
  print("not leap year")