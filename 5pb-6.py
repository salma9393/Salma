#print datatype of each element in the list
ls=["hi",10,10.5]
for i in ls:
    print(type(ls))
    
#print string is palindrome or not
str1="mom"
if (str1==str1[::-1]):
    print("palindrome")
else:
    print("not an palindrome")
    
#reverse each word in string
ls="think champ private limited"
b=ls.split()
print(b)
for i in b:
    print(i[::-1])
    

#program to get common character in 2 strings
str1="think"
str2="champ"
print(set(str1) & set(str2))


#program to print count of vowels and consonants in a string
str1="think champ"
v=c=0
for i in str1:
    if i in "aeiouAEIOU":
        v+=1
    else:
        c+=1
print(v)
print(c)
