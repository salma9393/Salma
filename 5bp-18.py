
#handling zero division error in generators
def gen():
  for i in range (5):yield i if i!=3 else 1
obj=gen()
try: print(list(obj))
except zerodivisionError:print("error")



#program to count to digits of a number
num=123
count=0
while num!=0:
  count+=1
  num=num//10
print(count)

#program to find  the sum of digits of a number
num=123
sum=0
while num!=0:
  rem=num%10
  sum=sum+rem
  num=num//10
print(sum)

#python program that prints the multiplication table
num=5
for i in  range(1,11):
  print(num,"*",i,"=" ,num*i)

#program that prints the multiplication tables from 1 to 10
for i in range(1,11):
  for j in range(1,11):
    print(f"{i*j}")
print()



