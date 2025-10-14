
#convert a list of strings to upper case
list1=["think","champ","private"]
print(list(map(str.upper,list1)))

#remove odd numbers from list
ls=[1,2,3,4,6,5]
print(list(filter(lambda x: x%2==0,ls)))

#format a string using format method
str1="think"
num=20
str2="champ"
print("str1:{},str2:{},num:{}".format(str1,str2,num))

#print floating numbers within 2 decimal values
num=10.56789345
print("%2f"%(num))

num=10.56789345
print(round(num,2))