class Customer:
    
    def __init__(self,name="NA",phoneNumber="0"):
        self.__name = name
        self.__phoneNumber = phoneNumber

    def __str__(self):
        return "The customer name is {}\nPhone number is {}".format(self.__name, self.__phoneNumber)
    
    

