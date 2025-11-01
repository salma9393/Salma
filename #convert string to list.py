#convert a string to list
fruits="apple banana mango"
print(fruits.split())


fruits="apple;mango;banana"
print(fruits.split(";"))


fruits="apple and mango and banana"
print(fruits.split("and"))