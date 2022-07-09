from PizzaOrder import PizzaOrder
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from Pizza import Pizza
from OrderQueue import OrderQueue

def test_Pizza():
    p1 = Pizza("S")
    p2 = Pizza("M")
    p3 = Pizza("L")
    p4 = Pizza("M")
    assert p1.getPrice() == 0.0
    assert p1.getSize() == "S"
    assert p2.getPrice() == 0.0
    assert p2.getSize() == "M"
    assert p3.getPrice() == 0.0
    assert p3.getSize() == "L"
    p4.setPrice(4.00)
    assert p4.getPrice() == 4.00
    assert p4.getSize() == "M"

def test_CustomPizza():
    p1 = CustomPizza("S")
    p2 = CustomPizza("M")
    p3 = CustomPizza("L")
    p4 = CustomPizza("M")
    assert p1.getPrice() == 8.00
    assert p1.getSize() == "S"
    assert p2.getPrice() == 10.00
    assert p2.getSize() == "M"
    assert p3.getPrice() == 12.00
    assert p3.getSize() == "L"
    p4.addTopping("bacon")
    p4.addTopping("pineapple")
    assert p4.getPrice() == 11.50
    assert p4.getPizzaDetails() == "CUSTOM PIZZA\nSize: M\nToppings:\n\t+ bacon\n\t+ pineapple\nPrice: $11.50\n"
    assert p3.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n"

def test_SpecialtyPizza():
    p1 = SpecialtyPizza("S", "Hawaiian")
    p2 = SpecialtyPizza("M", "Combo")
    p3 = SpecialtyPizza("L", "Pepperoni")
    assert p1.getPrice() == 12.00
    assert p1.getSize() == "S"
    assert p2.getPrice() == 14.00
    assert p2.getSize() == "M"
    assert p3.getPrice() == 16.00
    assert p3.getSize() == "L"
    assert p1.getPizzaDetails() == "SPECIALTY PIZZA\nSize: S\nName: Hawaiian\nPrice: $12.00\n"
    assert p2.getPizzaDetails() == "SPECIALTY PIZZA\nSize: M\nName: Combo\nPrice: $14.00\n"
    assert p3.getPizzaDetails() == "SPECIALTY PIZZA\nSize: L\nName: Pepperoni\nPrice: $16.00\n"

def test_PizzaOrder():
    p1 = CustomPizza("S")
    p2 = SpecialtyPizza("M", "Combo")
    p3 = CustomPizza("M")
    p3.addTopping("bacon")
    p3.addTopping("pineapple")
    p4 = PizzaOrder()
    p4.setTime(123000)
    p4.addPizza(p1)
    p4.addPizza(p2)
    p4.addPizza(p3)
    assert p4.getOrderDescription() == "******\nOrder Time: 123000\nCUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n\n----\nSPECIALTY PIZZA\nSize: M\nName: Combo\nPrice: $14.00\n\n----\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ bacon\n\t+ pineapple\nPrice: $11.50\n\n----\nTOTAL ORDER PRICE: $33.50\n******\n"      

def test_OrderQueue():
    p1 = CustomPizza("S")
    p2 = SpecialtyPizza("M", "Combo")
    p3 = CustomPizza("M")
    p3.addTopping("bacon")
    p3.addTopping("pineapple")
    p4 = PizzaOrder(1230000)
    p4.addPizza(p1)
    p5 = PizzaOrder(1330000)
    p5.addPizza(p2)
    p6 = PizzaOrder(100000)
    p6.addPizza(p3)
    p7 = OrderQueue()
    p7.addOrder(p4)
    p7.addOrder(p5)
    p7.addOrder(p6)
    assert p7.processNextOrder() == "******\nOrder Time: 100000\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ bacon\n\t+ pineapple\nPrice: $11.50\n\n----\nTOTAL ORDER PRICE: $11.50\n******\n"