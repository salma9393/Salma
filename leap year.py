#check leap year or notleap year
year=2028
if(year%400==0 and year%100==0):
    print("leap year")
elif(year%4==0 and year%100!=0):
    print("leap year")
else:
    print("non leap year")


#check leap year in another way
def is_leap(year):
    if(year%400==0 and year%100==0):
        print("leap year")
    elif(year%4==0 and year%100!=0):
        print("leap year")
    else:
        print("non leap year")

print(is_leap(2030))