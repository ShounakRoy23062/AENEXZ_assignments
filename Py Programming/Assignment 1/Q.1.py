username = input("Enter your Username: ")

if len(username)<5:
    print("Invalid Username. Username must contain at least 5 characters !")

elif username.isspace():
    print("Invalid Username. Username cannot contain only spaces !")

elif username.lower() == "admin":
    print("Invalid Username. Username cannot be 'admin' !")

else:
    print("Valid Username!")