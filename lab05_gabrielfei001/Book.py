#Book object
class Book:
    def __init__(self, title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year
    
    def getBookDetails(self):
        txt = "Title: {}, Author: {}, Year: {}"\
            .format(self.title, self.author, self.year)
        return txt
    
    def __gt__(self, rhs):
        if (self.author.upper() > rhs.author.upper()):
            return True
        if (self.author.upper() == rhs.author.upper()):
            if (self.year > rhs.year):
                return True
        if (self.year == rhs.year):
            if (self.title.upper() > rhs.title.upper()):
                return True
        return False