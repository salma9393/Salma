#product of a numbers
num=123
product=1
while num!=0:
    digit=num%10
    product*=digit
    num=num//10
print(product)
