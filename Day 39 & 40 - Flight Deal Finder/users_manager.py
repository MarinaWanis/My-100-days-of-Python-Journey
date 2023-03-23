from data_manager import DataManager

firstName=""
lastName=""
email=""
email2=""

def get_user_details():
    global firstName,lastName,email,email2
    firstName = input("What is you first name?: ")
    lastName = input("What is you last name?: ")
    email = input("Enter your email address: ")
    email2 = input("Enter your email address again for verification: ")


get_user_details()
if firstName =="" or lastName =="" or email =="" or email2 =="":
    print("Your registration is not complete since you data is incomplete")
    get_user_details()

elif email == email2:
    print("Your registration is completed You will receive great flight deals!")
    data_manager = DataManager()
    data_manager.add_users(firstName, lastName, email)
else:
    print("Your email is not matching Please re-enter your details ")
    get_user_details()
