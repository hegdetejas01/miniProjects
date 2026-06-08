class Keeper:

    __counter = 0

    __emp = {'tejas@gmail':['tejas','m','1234'],'google@gmail':['google','f','1234']}
    
    def __init__(self):
        self.__name = ""
        self.__email = ""
        self.__gender = ""
        self.__password = ""

    def loginEmployee(self):
        validCredential = False
        email = input("Enter your email: ")

        if email in Keeper.__emp:
            Keeper.__counter += 1
            password = input("Enter your password: ")

            if password == Keeper.__emp[email][2]:
                self.__password = password
                self.__email = email
                self.__gender = Keeper.__emp[email][1]
                self.__name = Keeper.__emp[email][0]
                validCredential = True
            
            else: 
                print("Incorrect Password")

                if Keeper.__counter < 3:
                    validCredential = self.loginEmployee()

                else:
                    print("Login limit exceeded\nTry again after sometime")

        else:
            print("Employee not registered.\nContact Admin to get registered.")

        print("Returning Value is ", validCredential)
        return validCredential
    
    def createMainMenu(self, name):
        print("Welcome", str(name).capitalize())
        keeperInput = int(input("""
1. Press 1 to "Make a bill"
2. Press 2 to "Add a product"
3. Press 3 to "Logout"
"""))
        return keeperInput
    
    def getData(self, parameter):
        if parameter == "name":
            return self.__name
        elif parameter == "gender":
            return self.__gender
        elif parameter == "email":
            return self.__email


