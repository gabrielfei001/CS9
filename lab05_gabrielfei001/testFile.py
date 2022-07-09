#Test File
from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode

def test_BookFuncs():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    b1 = Book("Cujo", "King, Stephen", 1981)
    assert b.getTitle() == "Ready Player One"
    assert b1.getTitle() == "Cujo"
    assert b.getAuthor() == "Cline, Ernest"
    assert b1.getAuthor() == "King, Stephen"
    assert b.getYear() == 2011
    assert b1.getYear() == 1981
    assert (b > b1) == False
    assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"
    assert b1.getBookDetails() == "Title: Cujo, Author: King, Stephen, Year: 1981"

def test_BookNodeFuncs():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    b2 = BookCollectionNode(b)
    assert b2.getNext() == None
    assert b2.getData() == b
    
def test_BookCollectionFuncs():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    assert bc.isEmpty() == True
    bc.insertBook(b0)
    assert bc.isEmpty() == False
    assert bc.getBooksByAuthor("King, Stephen") == "Title: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.getAllBooksInCollection() ==  "Title: Cujo, Author: King, Stephen, Year: 1981\n"
    bc.insertBook(b1)
    assert bc.getBooksByAuthor("King, Stephen") == "Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.getAllBooksInCollection() == "Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    bc.insertBook(b2)
    assert bc.getBooksByAuthor("King, Stephen") == "Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.getBooksByAuthor("Cline, Ernest") == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n"
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    bc.insertBook(b3)
    assert bc.getBooksByAuthor("King, Stephen") == "Title: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.getBooksByAuthor("Cline, Ernest") == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n"
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\nTitle: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"