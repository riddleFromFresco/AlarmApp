from datetime import datetime

import pytest


def test_checkString_True(funcToTest):
    vals = ["22:00", "0:00", "23:59"]
    for val in vals:
        assert (funcToTest(val), True)

def test_checkString_False(funcToTest):
    vals = ["222:00", "10:000", "-3:55", "2:61"]
    for val in vals:
        assert (funcToTest(val), False)


def test_isTimeToRing_True(funcToTest2):
    val = datetime.now().strftime("%H:%M").split(":")
    res = funcToTest2(val[0], val[1])

    assert (res)

def test_isTimeToRing_False(funcToTest2):
    val = (datetime.now() + timedelta(hours=2)).strftime("%H:%M").split(":")
    res = funcToTest2(val[0], val[1])

    assert (res, False)


def test_getWindow(funcToTest3):
    expectedName = "NewWindow"
    expectedSize = (100, 150)

    window = funcToTest3(expectedName, expectedSize)
    actualName = window.title()
    actualSize = (window.winfo_screenwidth(), window.winfo_screenheight())

    assert (expectedName == actualName)
    assert (expectedSize == actualSize)
