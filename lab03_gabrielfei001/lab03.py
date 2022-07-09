#lab03
def multiply(x, y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return (x + multiply(x, (y - 1)))

def collectOddValues(listOfInt):
    if len(listOfInt) == 0:
        return []
    if listOfInt[0]%2 == 1:
        return [listOfInt[0]] + collectOddValues(listOfInt[1:])
    else:
        return collectOddValues(listOfInt[1:])

def countInts(listOfInt, num):
    result = 0
    if len(listOfInt) == 0:
        return 0
    if listOfInt[0] == num:
        result = result + 1
        return result + countInts(listOfInt[1:], num)
    else:
        return countInts(listOfInt[1:], num)

def reverseString(s):
    if s == "":
        return ""
    return s[-1] + reverseString(s[:-1])

def removeSubString(s, sub):
    if sub not in s:
        return s
    if sub in s:
        return removeSubString(s.replace(sub,""),sub)
