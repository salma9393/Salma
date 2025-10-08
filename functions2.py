
#local variables and global variables
x=100
def fun():
  x=50
  print("inside function:",x)
fun()
print("outside function:",x)

#recursion in functions
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n * factorial(n-1)
print(factorial(5))

#nested functions
def outer():
  def inner():
    return"hello from inner function"
  return inner()
print(outer())

#function as argument
def square (x):
  return x*x
def apply(func,value):
  return func(value)
print(apply(square,3))