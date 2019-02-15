import random as r

class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.patrons = []
        self.available_books = []
        self.patron_name = []

    def add_patron(self, patron):
        self.patrons.append(patron)
        num = ""
        for i in range(5):
            num += str(r.randint(0,9))
        patron.acc_num = int(num)

    def lend(self, patron, book):
        if patron in self.patron:
            if book in self.available_books:
                Patron.books(book)
                self.available_books.pop(book)

    def add_book(self, book):
        self.available_books.append(book)

    def __repr__(self):
        output = ('Name: '+self.name+'\nLocation: '+self.location+'\nAvailable books: ')
        for i in self.available_books:
            output += "\n"+i

        for patron in self.patrons:
            output += "\n\nLibrary Patron Information:\nName: "+ patron.name+"\nLibrary Account Number: "+str(patron.acc_num)+'\n\nBorrowed Books: '
            for i in patron.books:
                output += '\n'+i
        return output


class Patron:
    def __init__(self, name):
        self.name = name
        self.acc_num = None
        self.books = []

def main():
    bk_library = Library("Brooklyn Public Library", "6 Metrotech Center")
    bk_library.add_book("Ender's Game")
    bk_library.add_book("Ender's Shadow")
    bk_library.add_book("Shadow of the Hegemon")
    bk_library.add_book("Ready Player One")
    bk_library.add_book("The Outsiders")
    bk_library.add_book("Flowers for Algernon")
    bob = Patron('Bob')
    bk_library.add_patron(bob)
    print(bob.acc_num)
    print(bk_library)


main()
