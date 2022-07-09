from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time = 0):
        self.pizzas = []
        self.time = time
    
    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time
    
    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        total = 0.00
        txt = "******\nOrder Time: " + str(self.time) + "\n"
        if len(self.pizzas) > 0:
            for i in range(len(self.pizzas)):
                total += self.pizzas[i].getPrice()
                txt += self.pizzas[i].getPizzaDetails() + "\n"
                txt += "----\n"
            txt += "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(total)
        else:
            txt += "----\n"
            txt += "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(total)
        return txt