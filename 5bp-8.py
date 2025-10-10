
#sum of values in the dictionary
dict={1:10,2:20,3:30}
print(sum(dict.values()))


dict={1:10,2:20,3:30}
sum=0
for i in dict.values():
  sum+=i
print(sum)


#find the maximum value in the dictionary
dict={1:10,2:20,3:30}
print(max(dict.values()))


#find the number of words in the sentence
a="think champ private limited"
print(len(a.split()))


#find the longest word in sentence
a="think champ private limitedruyfjhv"
print(max(a.split(),key=len))


#sqrt of a number
sr=49**(1/2)
print(sr)