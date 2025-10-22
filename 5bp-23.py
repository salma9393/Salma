

#pick a random character in a string
import random
str="think champ"
print(random.choice(str))


#generate an 8 characterpassword with uppercase,digit lowercase and symbols
import random
import string
password="".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=8))
print(password)


#generate a RGB colour code
import random
colour=random.randint(0,255),random.randint(0,255),random.randint(0,255)
print(colour)


#generate a muliplication question eith a random numbers between 1 and 12
import random
num1,num2=random.randint(1,12),random.randint(1,12)
print("what is {}*{}? answer is{}".format(num1,num2,num1*num2))


#generate a random odd numbers between 1 and 9
import random
print(random.randrange(1,20,2))