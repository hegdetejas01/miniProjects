import printStatement as p

class Products:

    def __init__(self,itemName,amount):
        self.__itemName = itemName
        self.__amount = amount

class Books(Products):

    def __init__(self,bookName, amount):
        if self.__class__.__name__ == "PaperBooks":
            self.__category = "paperbook"
        elif self.__class__.__name__ == "AudioBooks":
            self.__category == "audiobook"
        super().__init__(bookName, amount)

class PaperBooks(Books):

    def __init__(self):
        bookName = input(p.get_book_name)
        amount = input(p.get_book_amount)
        pages = input(p.get_number_of_pages)
        self.__pages = pages
        super().__init__(bookName, amount)

    def addPaperBook(self):
        pass

class AudioBooks(Books):

    def __init__(self):
        audioBookName = input(p.get_audio_book_name)
        amount = input(p.get_audio_book_amount)
        duration = input(p.get_audio_book_duration_in_minutes)
        self.__duration = duration
        super().__init__(audioBookName, amount)

    def addAudioBook(self):
        pass

class Stationaries(Products):
    pass