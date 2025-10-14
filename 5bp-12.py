
#intersection of two numberswhose sum of digits are divisible by 3
s1={1,2,3,4,5,6,18,10}
s2={34,15,18,12}
s3={x for x in s1.intersection(s2)if sum([int(i) for i in str(x)])}
print(s3)

#find the occurance of a particular char in string and return index
str="think champ"
print(str.index("h"))
print(str.find("h"))

str="think champ"
print(str.rindex("h"))
print(str.rfind("h"))

#convert half of string into reverse and half into normal order
str="think champ"
hal=len(str)//2
print(hal)
print(str[:hal]+str[hal:])

#printing even numbers from user input in list of values
user=input()
num=list(map(int,user.split()))
print(list(filter(lambda x:x%2==0,num)))

#square eachvalue in list using map
user=input()
num=list(map(int,user.split()))
print(list(map(lambda x:x**3,num)))