class Keeper:

    __emp = {'tejas@gmail':['tejas','m','1234'],'google@gmail':['google','f','1234']}
    
    def __init__(self):
        pass

    def loginEmployee(self):
        email = input("Enter your email: ")
        if email in Keeper.__emp:
            password = input("Enter your password: ")
            if password == Keeper.__emp[email][2]:
                print("Login Successfull :)")
            else: print("Incorrect Password")
        else:
            print("Employee not registered.\nContact Admin to get registered.")


