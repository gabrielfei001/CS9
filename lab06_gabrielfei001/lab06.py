from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]: #might need to change to just <
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1

def ensureSortedAscending(apartmentList):
    if len(apartmentList) < 1:
        return False
    if len(apartmentList) == 1:
        return True
    if len(apartmentList) > 1:
        i = 1
        ascending = True
        while i < len(apartmentList):
            if (apartmentList[i] < apartmentList[i - 1]):
                ascending = False
            i = i + 1
    return ascending

def getNthApartment(apartmentList, n):
    if (n-1) in range(len(apartmentList)):
        return apartmentList[n-1].getApartmentDetails()
    else:
        return "(Apartment " + str(n) + ") DNE"

def getTopThreeApartments(sorted_apartmentList):
    txt = ""
    if len(sorted_apartmentList) >= 3:
        txt = "1st: " + sorted_apartmentList[0].getApartmentDetails() + ", 2nd: " + sorted_apartmentList[1].getApartmentDetails() + ", 3rd: " + sorted_apartmentList[2].getApartmentDetails()
    if len(sorted_apartmentList) < 3:
        if len(sorted_apartmentList) == 2:
            txt = "1st: " + sorted_apartmentList[0].getApartmentDetails() + ", 2nd: " + sorted_apartmentList[1].getApartmentDetails()
        if len(sorted_apartmentList) == 1:
            txt = "1st: " + sorted_apartmentList[0].getApartmentDetails()
    return txt

