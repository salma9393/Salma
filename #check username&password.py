#check username&password
username="ADMIN"
password="93930"
user_input=input("enter username:")
password_input=input("enter the password:")
if username==user_input and password==password_input:
    print("login sucessfully")
else:
    print("invalid login")