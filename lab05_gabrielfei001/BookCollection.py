#Book Collection
from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        total = 0
        temp = self.head
        while temp != None:
            total += 1
            temp = temp.getNext()
        return total
    
    def insertBook(self, book):
        current = self.head
        previous = None
        inserted = False
        while (current != None and inserted != True):
            if current.data > book:
                inserted = True
            else:
                previous = current
                current = current.getNext()
        temp = BookCollectionNode(book)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)    

    def getBooksByAuthor(self, author):
        txt = ""
        temp = self.head
        while temp != None:
            if (temp.data.author.upper() == author.upper()): #infinitely looping
                txt += temp.data.getBookDetails() + "\n"
                temp = temp.getNext()
            else:
                temp = temp.getNext()
        return txt

    def getAllBooksInCollection(self):
        txt = ""
        temp = self.head
        while temp != None:
            txt = txt + temp.data.getBookDetails() + '\n'
            temp = temp.getNext()
        return txt


