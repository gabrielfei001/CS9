from Card import Card
class PlayerHand:
    def __init__(self):
        self.root = None
        self.size = 0

    def getTotalCards(self):
        return self.size
    
    def getMin(self):
        if self.size == 0:
            return None
        else:
            currentCard = self.root
            while currentCard.left:
                currentCard = currentCard.left
            return currentCard
    
    def getSuccessor(self, suit, rank):
        if type(suit) == str:
            suit = suit.upper()
        if type(rank) == str:
            rank = rank.upper()
        succCard = self.get(suit, rank)
        temp = self.root
        if succCard == None:
            return None
        else:
            successor = None
            if succCard.right:
                self.root = succCard.right
                successor = self.getMin()
                self.root = temp
            else:
                if succCard.parent():
                    if succCard.isLeft():
                        successor = succCard.parent
                    elif succCard.isRight():
                        succCard.parent.right = None
                        successor = self.getSuccessor(succCard.parent.suit, succCard.parent.rank)
                        succCard.parent.right = succCard
                else:
                    return None
            return successor
    
    def put(self, suit, rank):
        if self.root:
            self._put(suit, rank, self.root)
        else:
            self.root = Card(suit, rank)
        self.size += 1

    def _put(self, suit, rank, currentCard): #check if card exists already, done
        insertCard = Card(suit, rank)
        # insertCard.convertCard()
        if currentCard != None:
            # currentCard.convertCard()
            if insertCard == currentCard: #maybe need to insert insertCard
                # insertCard.convertCardBack()
                # currentCard.convertCardBack()
                currentCard.count = currentCard.count + 1
            elif insertCard < currentCard:
                if currentCard.getLeft():
                    # currentCard.convertCardBack()
                    self._put(suit, rank, currentCard.left)
                else:
                    # insertCard.convertCardBack()
                    # currentCard.convertCardBack()
                    currentCard.left = insertCard
                    currentCard.left.parent = currentCard
            else:
                if currentCard.getRight():
                    # currentCard.convertCardBack()
                    self._put(suit, rank, currentCard.right)
                else:
                    # insertCard.convertCardBack()
                    # currentCard.convertCardBack()
                    currentCard.right = insertCard
                    currentCard.right.parent = currentCard

    def delete(self, suit, rank):
        if self.size > 1:
            cardToRemove = self._get(suit, rank, self.root)
            if cardToRemove != None:
                if cardToRemove.count > 1: #first need to check how many cards, done
                    cardToRemove.count = cardToRemove.count - 1
                    self.size = self.size - 1
                    return True
                if cardToRemove.count == 1:
                    self.remove(cardToRemove)
                    self.size = self.size - 1
                    return True
            else:
                return False
        elif self.size == 1 and self.root.suit == suit and self.root.rank == rank:
            self.root = None
            self.size = self.size - 1
            return True
        else:
            return False

    def remove(self, currentCard):
        if currentCard != None:
            # currentCard.convertCard()
            if currentCard.isLeaf():
                # currentCard.parent.left.convertCard() #Case 1: Card to remove is a leaf, also need to check num of cards
                if currentCard == currentCard.parent.left:
                # if currentCard.count > 1:
                #     currentCard.count = currentCard.count - 1
                # if current
                    # currentCard.convertCardBack()
                    # currentCard.parent.left.convertCardBack()
                    currentCard.parent.left = None
                else:
                    # currentCard.convertCardBack()
                    # currentCard.parent.left.convertCardBack()
                    currentCard.parent.right = None
            elif currentCard.hasBothChildren(): #Case 3: Card to remove has both children, also need to check num of cards
                succ = self.getSuccessor(currentCard.suit, currentCard.rank)
                succ.spliceOut()
                currentCard = succ
            else: #Case 2: Card to remove has one child, also need to check num of cards
                if currentCard.getLeft():
                    if currentCard.isLeft():
                        currentCard.left.parent = currentCard.parent
                        currentCard.parent.left = currentCard.isLeft
                    elif currentCard.isRight():
                        currentCard.left.parent = currentCard.parent
                        currentCard.parent.right = currentCard.left
                    else:
                        currentCard.replaceCardData(currentCard.left.suit, currentCard.left.rank, 
                        currentCard.left.count, currentCard.left.left, currentCard.left.right)

    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def get(self, suit, rank):
        if self.root != None:
            res = self._get(suit, rank, self.root)
            if res != None:
                return res
            else:
                return None
        else:
            return None

    def _get(self, suit, rank, currentCard):
        findCard = Card(suit, rank)
        # findCard.convertCard()
        if currentCard != None:
            # currentCard.convertCard()
            if findCard == currentCard:
                # findCard.convertCardBack()
                # currentCard.convertCardBack()
                return currentCard
            elif findCard < currentCard:
                # findCard.convertCardBack()
                # currentCard.convertCardBack()
                return self._get(suit, rank, currentCard.left)
            else:
                # findCard.convertCardBack()
                # currentCard.convertCardBack()
                return self._get(suit, rank, currentCard.right)
        else:
            return None
        
    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, currentCard):
        ret = ""
        if currentCard != None:
            ret += self._inOrder(currentCard.getLeft())
            ret += currentCard.__str__()
            ret += self._inOrder(currentCard.getRight())
        return ret

    def preOrder(self):
        return self._preOrder(self.root)
    
    def _preOrder(self, currentCard):
        ret = ""
        if currentCard != None:
            ret += currentCard.__str__()
            ret += self._preOrder(currentCard.getLeft())
            ret += self._preOrder(currentCard.getRight())
        return ret
