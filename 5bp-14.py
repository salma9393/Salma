
#remove all elements greater than given from a set
s1={10,20,30}
t=20
for x in list(s1):
  if x>t:
    s1.remove(x)
print(s1)

#check if number is multiple of both 3 and 5
num=15
if num%3==0 and num%5==0:
  print("yes, it is divisible by both 3 and 5")
elif(num%3==0):
  print("divisible by 3")
else:
  print("divisible by 5")

#program to find  number as positive ,negative ,even odd
num=15
if (num%2==0)and num>0:
  print("even positive number")
elif(num%2==0) and num<0:
  print("even negative number")
elif(num%2!=0) and num<0:
  print("odd negative number")
else:
  print("odd positive number")

#program to check whether  anumber is 3 digit or not
num=321
num1=str(num)
if len(num1)==3:
  print("it is 3 digit number")
else:
  print("it is not a 3 digit number")

#program to check a character is vowel or not
ch="e"
if ch in "aeiouAEIOU":
  print("yes it is vowel")
else:
 ("no it is not vowel")