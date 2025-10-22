
#program to print random numbers
import random
print(random.randrange(1,10))
print(random.randint(1,5))



#given an integer perform the following conditional actions
#if n is odd,print weird
#if n is even and in the,inclusive range 2 to 5 print not weird
#if n is even and in the inclusive range of 6 to 20 print weird
#if n is even and greater than 20 print not weird
n=int(input())
if n%2!=0:
  print("weird")
elif n%2==0 and n>2 and n<5:
  print("not weird")
elif n%2==0 and n>6 and n<20:
  print("weird")
else:
  print("not weird")


#program for tet wrap
import textwrap
word="wings of fire"
print(textwrap.fill(word,2))



#python code to compute average of marks for a specified student
marks=[20.45,10,38,47,59]
n=len(marks)
avg=sum(marks)/n
print(avg)


#randomly shuffle elements in the list
import random
ls=[20,40,60,80,50]
random.shuffle(ls)
print(ls)

