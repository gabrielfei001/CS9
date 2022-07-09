from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if self.size == "S":
            Pizza.setPrice(self, 12.00)
            #self.price = 12.00
        if self.size == "M":
            Pizza.setPrice(self, 14.00)
            #self.price = 14.00
        if self.size == "L":
            Pizza.setPrice(self, 16.00)
            #self.price = 16.00

    def getPizzaDetails(self):
        txt = "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n"\
                .format(self.size, self.name, Pizza.getPrice(self))
        return txt