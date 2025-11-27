#functions-19,20
def welcome():
    print("you are welcome")
    print("python")
welcome()


def welcome (name):
    print(f"hello {name}")
user=input ("enter your name:")
welcome(user)

def toss():
    print("press 1 to select heads")
    print("press2 to select toss")
    choice=int(input("type your choice:"))
    return choice
my_choice=toss()
if my_choice==1:
    print("heads")
else:
    print("trails")


def add(a,b):
    c=a+b
    return c
    x=int(input())
    y=int(input())
print(add(x,y))

