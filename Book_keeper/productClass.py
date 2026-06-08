class Products:

    def __init__(self,itemName,amount):
        self.__itemName = itemName
        self.__amount = amount

class Books(Products):
    pass

class PaperBooks(Books):
    pass

class AudioBooks(Books):
    pass

class Stationaries(Products):
    pass