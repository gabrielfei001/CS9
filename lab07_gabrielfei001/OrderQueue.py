from PizzaOrder import PizzaOrder
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from Pizza import Pizza

class OrderQueue:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].getTime() < self.heapList[i//2].getTime():
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def precDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].getTime() > self.heapList[mc].getTime():
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].getTime() < self.heapList[i*2+1].getTime():
                return i * 2
            else:
                return i * 2 + 1

    def addOrder(self, pizzaOrder):
        self.heapList.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize) #change perc up, smaller the value

    def processNextOrder(self):
        try:
            if self.currentSize == 0:
                raise QueueEmptyException()
        except QueueEmptyException:
            print("Exception of type QueueEmptyException caught!")
        retval = self.heapList[1].getOrderDescription()
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.precDown(1) #change perc down
        return retval

class QueueEmptyException(Exception):
    pass