#testFile
import pytest
from lab03 import multiply
from lab03 import collectOddValues
from lab03 import countInts
from lab03 import reverseString
from lab03 import removeSubString

def test_Multiply():
    assert (6 *4) == multiply(6, 4)
    assert (9 * 8) == multiply(9, 8)
    assert (15 * 24) == multiply(15, 24)
    assert (3 * 3) == multiply(3, 3)
    assert (20 * 20) == multiply(20, 20)

def test_zeroMultiply():
    assert (7 * 0) == multiply(7, 0)
    assert (1934583 * 0) == multiply(1934583, 0)
    assert (342 * 0) == multiply(342, 0)
    assert (0 * 754) == multiply(0, 754)
    assert (0 * 123) == multiply(0, 123)

def test_oneMultiply():
    assert (1 * 23) == multiply(1, 23)
    assert (34 * 1) == multiply(34, 1)
    assert (0 * 1) == multiply(0, 1)
    assert (72 *1) == multiply(72, 1)
    assert (1 * 99) == multiply(1, 99)

def test_collectOddValues():
    assert [1, 3, 5] == collectOddValues([1,2,3,4,5])
    assert [5, 7] == collectOddValues([2,4,5,6,7,8])
    assert [1, 7, 9] == collectOddValues([1,4,6,7,9,10])
    assert [11] == collectOddValues([2,4,6,8,11])

def test_collectNoValues():
    assert [] == collectOddValues([2,4,6])
    assert [] == collectOddValues([])
    assert [] == collectOddValues([4])

def test_collectOneValueList():
    assert [1] == collectOddValues([1])
    assert [5] == collectOddValues([5])
    assert [7] == collectOddValues([7])

def test_countInts():
    assert countInts([1,2,3,4,3,2,1], 2) == 2
    assert countInts([4, 2, 3, 3, 1, 3], 3) == 3
    assert countInts([23, 24, 15, 377, 3], 23) == 1

def test_oneItemListCountInts():
    assert countInts([1], 1) == 1
    assert countInts([4], 4) == 1
    assert countInts([6], 5) == 0

def test_emptyListCountInts():
    assert countInts([], 3) == 0
    assert countInts([], 1) == 0
    assert countInts([], 7) ==0

def test_sameItemListCountInts():
    assert countInts([3,3,3,3,3], 3) == 5
    assert countInts([1,1,1,1,1,1,1,1], 1) == 8
    assert countInts([4,4,4,4,4,4], 1) == 0

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("codingassignment") == "tnemngissagnidoc"
    assert reverseString("helloworld") == "dlrowolleh"

def test_emptyReverseString():
    assert reverseString (" ") == " "
    assert reverseString("") == ""

def test_sameLetterReverseString():
    assert reverseString("aaaaaaa") == "aaaaaaa"
    assert reverseString("AAAAAAA") == "AAAAAAA"
    assert reverseString("1111111") == "1111111"

def test_removeSubString():
    assert removeSubString("sugarbrownsugarsalt","sugar") == "brownsalt"
    assert removeSubString("oxygenandoxygenandhydrogeniswater","oxygen") == "andandhydrogeniswater"
    assert removeSubString("iamonewiththeforceandtheforceiswithme","force") == "iamonewiththeandtheiswithme"

def test_multipleremoveSubString():
    assert removeSubString("Lololololol", "lol") == "Loool"
    assert removeSubString("dooodooo", "oo") == "dodo"
    assert removeSubString("mhmhmhmhmhmhmkay", "mhm") == "hhhmkay"

def test_emptyRemoveSubString():
    assert removeSubString("weeeehoooo", "") == "weeeehoooo"
    assert removeSubString("","YEP") == ""

def test_notInRemoveSubString():
    assert removeSubString("a;lwknef;lne", "okkayyyy") == "a;lwknef;lne"
    assert removeSubString("morecodingyay", "bleh") == "morecodingyay"