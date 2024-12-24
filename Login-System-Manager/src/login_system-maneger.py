user = "Yasin"
password = "1234"

while True:
    username_input = input("Enter your Username: ")
    password_input = input("Enter your Password: ")

    if username_input == user and password_input == password:
        print(user, "Welcome!")
        break
    elif username_input != user and password_input == password:
        print("Incorrect Username!")
        print("If you forgot your username, press 'Y'. Otherwise, press 'N'.")
        response1 = input()
        if response1 == "Y":
            new_username = input("Enter a new Username: ")
            user = new_username
            print("Your Username has been successfully updated!")
    elif username_input == user and password_input != password:
        print("Incorrect Password!")
        print("If you forgot your password, press 'Y'. Otherwise, press 'N'.")
        response2 = input()
        if response2 == 'Y':
            new_password = input("Enter a new Password: ")
            password = new_password
            print("Your Password has been successfully updated!")
    else:
        print("Try again.")
