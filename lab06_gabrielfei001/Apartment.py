class Apartment:
    def __init__(self, rent = 0.0, metersFromUCSB = 0, condition = 0):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        txt = "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}/10"\
            .format(self.rent, self.metersFromUCSB, self.condition)
        return txt

    def __gt__(self, rhs):
        if self.rent > rhs.rent:
            return True
        if self.rent == rhs.rent:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
        if self.metersFromUCSB == rhs.metersFromUCSB:
            if self.condition < rhs.condition:
                return True
        return False

    def __lt__(self, rhs):
        if self.rent < rhs.rent:
            return True
        if self.rent == rhs.rent:
            if self.metersFromUCSB < rhs.metersFromUCSB:
                return True
        if self.metersFromUCSB == rhs.metersFromUCSB:
            if self.condition > rhs.condition:
                return True
        return False

    def __eq__(self, rhs):
        if self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and self.condition == rhs.condition:
            return True
        else:
            return False