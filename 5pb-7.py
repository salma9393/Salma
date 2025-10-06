#program to check if a substring is present in string
str="think champ private limited"
str1="champ" 
if str1 in str:
    print("exists")
else:
    print("does'nt exists")

#print that words that have an even number of characters
str="think champ private limited is a training platform"
str1=str.split()
print(str1)
for i in str1:
    if len(i)%2==0:
        print(i)

#remove duplicate words from a string
str="think champ private limited think champ "
str1=str.split()
b=[]
for x in str1:
    if x not in b:
        b.append(x)
    print(b)
    print("".join(b))

#check if string contains special characters
str1="thinkchamp!@#$%&*45565"
count=1
for x in str1:
    if not(x.isalpha() or x.isdigit()):
        count+=1
        print(count)
        if count>0:
            print("exists")
        else:
            print("doesn't exits")


#swap keys and values in dictionary
dict={1:"ammu",2:"sara",3:"priya",4:"raji"}
dict1={value:key for key,value in dict.items()}
print(dict1)