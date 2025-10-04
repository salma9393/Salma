
#clear a list of elements
li=[1,2,3,4,5]
li.clear()
print(li)

li=[1,2,3,4,5]
del(li[:])
print(li)

#reverse a list
li=[1,2,3,4,5]
li.reverse()
print(li)

li=[1,2,3,4,5]
print(li[::-1])

li=[1,2,3,4,5]
print(list(reversed(li)))

li=[1,2,3,4,5,6,7,8,9]
rev=[]
for i in range(len(li)-1,-1,-1):
  rev.append(li[i])
print(rev)

#even numbers in a list
li=[1,2,3,4,5,6,7,8,9]
for i in li:
  if i%2==0:
    print(i)

#to print second largest number in list
li=[1,2,3,4,5,6,7,8,9]
li.sort()
print(li[-2])

#print duplicate values in list
li=[1,3,3,4,6,6,8,7,6,6,]
li2=[]
for i in  li:
  if li.count(i)>1 and i not in li2:
    li2.append(i)
print(li2)