class Card:
    def __init__(self, suit, rank):
        self.suit = suit.upper()
        self.rank = rank.upper()
        self.parent = None
        self.left = None
        self.right = None
        self.count = 1

    def getSuit(self):
        return self.suit

    def setSuit(self, suit):
        self.suit = suit.upper()

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank.upper()
    
    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = count
    
    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
    
    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def isLeft(self):
        return self.parent and self.parent.left == self

    def isRight(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeft():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.getRight():
                if self.isLeft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    # def convertCard(self):
    #     if self != None:
    #         if self.rank == "A":
    #             self.rank = "1"
    #         if self.rank == "J":
    #             self.rank = "11"
    #         if self.rank == "Q":
    #             self.rank = "12"
    #         if self.rank == "K":
    #             self.rank = "13"
    #         if self.suit == "C":
    #             self.suit = 0
    #         if self.suit == "D":
    #             self.suit = 1
    #         if self.suit == "H":
    #             self.suit = 2
    #         if self.suit == "S":
    #             self.suit = 3
    
    # def convertCardBack(self):
    #     if self != None:
    #         if self.rank == "1":
    #             self.rank = "A"
    #         if self.rank == "11":
    #             self.rank = "J"
    #         if self.rank == "12":
    #             self.rank = "Q"
    #         if self.rank == "13":
    #             self.rank = "K"
    #         if self.suit == 0:
    #             self.suit = "C"
    #         if self.suit == 1:
    #             self.suit = "D"
    #         if self.suit == 2:
    #             self.suit = "H"
    #         if self.suit == 3:
    #             self.suit = "S"

    def replaceCardData(self, suit, rank, count, left, right):
        self.suit = suit.upper()
        self.rank = rank.upper()
        self.count = count
        self.left = left
        self.right = right
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right.parent = self

    def __str__(self): #str()
        txt = "{} {} | {}\n"\
            .format(self.getSuit(), self.getRank(), self.getCount())
        return txt

    def __gt__(self, rhs): #fix this, done
        r = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        s = ['C', 'D', 'H', 'S']
        if (self.rank in r) and (rhs.rank in r):
            if r.index(self.rank) > r.index(rhs.rank):
                return True
            elif r.index(self.rank) > r.index(rhs.rank):
                return False
            elif r.index(self.rank) == r.index(rhs.rank):
                if s.index(self.suit) > s.index(rhs.suit):
                    return True
                else:
                    return False

    def __lt__(self, rhs): #fix this, done
        r = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        s = ['C', 'D', 'H', 'S']
        if (self.rank in r) and (rhs.rank in r):
            if r.index(self.rank) < r.index(rhs.rank):
                return True
            elif r.index(self.rank) > r.index(rhs.rank):
                return False
            elif r.index(self.rank) == r.index(rhs.rank):
                if s.index(self.suit) < s.index(rhs.suit):
                    return True
                else:
                    return False


    def __eq__(self, rhs): #fix this, done
        if rhs == None:
            return False
        if self.rank == rhs.rank and self.suit == rhs.suit:
            return True
        else:
            return False
