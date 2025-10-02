#interchanging the first and last element in list
li=[1,2,4,5,6]
temp=li[-1]
li[-1]=li[0]
li[0]=temp
print(li)

#swap two elements in the list
li=[2,3,4,5]
temp=li[2]
li[2]=li[1]
li[1]=temp
print(li)

#lenth of the list
li=[1,2,3,4,5,6,7,8,9]
print(len(li))

#count of element
li=[1,2,3,4,5,6,7,8,9]
count=0
for i in li:
  count+=1
  print(count)

#program to find elements exist in list
li=[1,2,3,4,5,6,7,8,9]
print(li.count(2))
print(4 in li)
if li.count(2)>0:
  print("exists")
else:
  print("doesn't exists" )