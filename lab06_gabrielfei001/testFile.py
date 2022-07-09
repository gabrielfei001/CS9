from Apartment import Apartment
from lab06 import mergesort, ensureSortedAscending, getNthApartment, getTopThreeApartments

a0 = Apartment(1204.56, 200, 3)
a1 = Apartment(1204.56, 200, 7)
a2 = Apartment(1000, 100, 9)
a3 = Apartment(1000, 214, 10)
a4 = Apartment(300, 112, 3)
a5 = Apartment(300.52, 250, 2)
apartmentList = [a0, a1, a2, a3, a4, a5]

def test_ApartmentFuncs():
    assert a0.getRent() == 1204.56
    assert a1.getRent() == 1204.56
    assert a2.getRent() == 1000
    assert a3.getRent() == 1000
    assert a4.getRent() == 300
    assert a5.getRent() == 300.52
    assert a0.getMetersFromUCSB() == 200
    assert a1.getMetersFromUCSB() == 200
    assert a2.getMetersFromUCSB() == 100
    assert a3.getMetersFromUCSB() == 214
    assert a4.getMetersFromUCSB() == 112
    assert a5.getMetersFromUCSB() == 250
    assert a0.getCondition() == 3
    assert a1.getCondition() == 7
    assert a2.getCondition() == 9
    assert a3.getCondition() == 10
    assert a4.getCondition() == 3
    assert a5.getCondition() == 2
    assert a0.getApartmentDetails() == "(Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 3/10"
    assert a1.getApartmentDetails() == "(Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 7/10"
    assert a2.getApartmentDetails() == "(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: 9/10"
    assert a3.getApartmentDetails() == "(Apartment) Rent: $1000, Distance From UCSB: 214m, Condition: 10/10"
    assert a4.getApartmentDetails() == "(Apartment) Rent: $300, Distance From UCSB: 112m, Condition: 3/10"
    assert a5.getApartmentDetails() == "(Apartment) Rent: $300.52, Distance From UCSB: 250m, Condition: 2/10"

def test_lab06Funcs():
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert getTopThreeApartments(apartmentList) == "1st: (Apartment) Rent: $300, Distance From UCSB: 112m, Condition: 3/10, 2nd: (Apartment) Rent: $300.52, Distance From UCSB: 250m, Condition: 2/10, 3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: 9/10"
    assert getNthApartment(apartmentList, 1) == "(Apartment) Rent: $300, Distance From UCSB: 112m, Condition: 3/10"
    assert getNthApartment(apartmentList, 2) == "(Apartment) Rent: $300.52, Distance From UCSB: 250m, Condition: 2/10"
    assert getNthApartment(apartmentList, 3) == "(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: 9/10"
    assert getNthApartment(apartmentList, 4) == "(Apartment) Rent: $1000, Distance From UCSB: 214m, Condition: 10/10"
    assert getNthApartment(apartmentList, 5) == "(Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 7/10"
    assert getNthApartment(apartmentList, 6) == "(Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 3/10"

def test_cornerCases():
    b0 = Apartment()
    assert b0.getRent() == 0.0
    assert b0.getMetersFromUCSB() == 0
    assert b0.getCondition() == 0
    b1 = Apartment(123, 456, 1)
    apartmentList1 = [b1]
    assert getNthApartment(apartmentList1, 2) == "(Apartment 2) DNE"
    assert getTopThreeApartments(apartmentList1) == "1st: (Apartment) Rent: $123, Distance From UCSB: 456m, Condition: 1/10"
    assert ensureSortedAscending(apartmentList1) == True