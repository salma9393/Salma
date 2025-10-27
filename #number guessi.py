#number guessi
import random

num=random.randint(1,10)
guess=int(input("guess a number:"))
print(num,guess)
if (num==guess):
    print("you are amazing")
else:
    print("please try again")