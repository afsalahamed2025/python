def logins():
    print("VAANGEE LOGIN PANNALAM")

    username = "afsal"
    password = "123"
    email    = "a@gmail.com"
    mobile   = "123"

    input_username = input("Enter The Username :")
    input_password = input("Enter The Password :")
    input_email = input("Enter The email :")
    input_mobile = input("Enter The Mobile :")
    if input_username == username and input_password == password and input_email == email and input_mobile == mobile:
        print("Login Successfully ")

    else:
        print("Please try again.")


logins()
