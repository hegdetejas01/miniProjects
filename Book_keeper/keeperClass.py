class Keeper:

    __counter = 0

    __emp = {'tejas@gmail':['tejas','m','1234'],'google@gmail':['google','f','1234']}
    
    def __init__(self):
        self.loginEmployee()

    def loginEmployee(self):
        email = input("Enter your email: ")
        if email in Keeper.__emp:
            Keeper.__counter += 1
            password = input("Enter your password: ")
            if password == Keeper.__emp[email][2]:
                print("Login Successfull :)")
            else: 
                print("Incorrect Password")
                if Keeper.__counter < 3:
                    self.loginEmployee()
                else:
                    print("Login limit exceeded\nTry again after sometime")
        else:
            print("Employee not registered.\nContact Admin to get registered.")

# emp = Keeper()


