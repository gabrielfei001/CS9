from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.topList = []
        if self.size == "S":
            Pizza.setPrice(self, 8.00)
            #self.price = 8.00
        if self.size == "M":
            Pizza.setPrice(self, 10.00)
            #self.price = 10.00
        if self.size == "L":
            Pizza.setPrice(self, 12.00)
            #self.price = 12.00

    def addTopping(self, topping):
        addon = 0.0
        if self.size == "S":
            addon = 0.50
        if self.size == "M":
            addon = 0.75
        if self.size == "L":
            addon = 1.00
        self.topList.append(topping)
        Pizza.setPrice(self, Pizza.getPrice(self) + addon)

    def getPizzaDetails(self):
        txt = "CUSTOM PIZZA\nSize: " + self.size + "\n"
        txt += "Toppings:\n"
        if len(self.topList) != 0:
            for i in range(len(self.topList)):
                txt += "\t+ " + self.topList[i] + "\n"
        txt += "Price: ${:.2f}\n".format(Pizza.getPrice(self))
        return txt

    