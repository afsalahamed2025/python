class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print("Login page")
        input_username = input("Enter The Username :")
        input_password = input("Enter The Password :")
        if (
                input_username == self.username
                and input_password == self.password

        ):
            print("Login Successfully")

        else:
            print("Login Failed.")


user1 = user("afsal", "123")
user1.login()
