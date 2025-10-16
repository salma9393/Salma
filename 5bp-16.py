
#finding factorial of a number (using for loop)
num,fact= 5,1
for i in range(1,num+1):
  fact=fact*i
print(fact)



#finding factors of a number using while loop
num=6
i=1
while (i<=num):
  if (num%i==0):
    print(i)
  i+=1



#printing only consonants and skipping vowels using for loop
str1="think champ"
for i in str1.lower():
  if i in "aeiou":
    continue
  print(i)



#program to zips two lists and sums the corresponding elements
l1=[10,20,30]
l2=[30,10,3]
print([x+y for x,y in zip(l1,l2)])



#program to prints each elements along  with it,s index
lis1=["think","champ","private","limited"]
for x,y  in enumerate(lis1):
  print(x,y)