
#cubes of n namtural numbers
n=4
cube=(((n*(n+1))//2)**2)
print(cube)

#sum of n natural numbers
n=4
sum=((n*(n+1))//2)
print(sum)

#fibonacci series
n=5
n1=0
n2=1
if n<0:
  print("enter a valid number")
elif n==1:
  print(n1)
else:
  while n>0:
    print(n1)
    next=n1+n2
    n1=n2
    n2=next
    n=n-1

#maximum element in array
import array
arr=array.array('i',[1,2,3,4,5])
print(max(arr))

#rotation of array
import array
arr=array.array('i',[1,2,3,4,5])
r=2
print(arr[r:]+arr[:r])