from datetime import datetime, timedelta

import pytest

from main import Application


@pytest.fixture
def funcToTest():
    app = Application()
    return app._checkString

@pytest.fixture
def funcToTest2():
    app = Application()
    return app._isTimeToRing

@pytest.fixture
def funcToTest3():
    app = Application()
    return app._getWindow

@pytest.fixture
def funcToTest4():
    app = Application()
    app.entry_val = datetime.now().strftime("%H:%M")
    app.show_message()
    res = app.label_val

    return res

@pytest.fixture
def funcToTest5():
    app = Application()
    app.entry_val = "222:223E"
    app.show_message()
    res = app.label_val

    return res

def test_checkString_True(funcToTest):
    vals = ["22:00", "00:00", "23:59"]
    for val in vals:
        assert (funcToTest(val), True)

def test_checkString_False(funcToTest):
    vals = ["222:00", "10:000", "-3:55", "2:61"]
    for val in vals:
        assert (funcToTest(val), False)


def test_isTimeToRing_True(funcToTest2):
    val = datetime.now().strftime("%H:%M").split(":")
    res = funcToTest2(int(val[0]), int(val[1]))

    assert (res)

def test_isTimeToRing_False(funcToTest2):
    val = (datetime.now() + timedelta(hours=2)).strftime("%H:%M").split(":")
    res = funcToTest2(int(val[0]), int(val[1]))

    assert (res, False)


def test_getWindow(funcToTest3):
    expectedName = "NewWindow"
    expectedSize = (150, 100)

    window = funcToTest3(expectedName, expectedSize)
    window.update()
    actualName = window.title()
    actualSize = (window.winfo_width(), window.winfo_height())
    window.destroy()
    assert (expectedName == actualName)
    assert (expectedSize == actualSize)


def test_showMessage_Correct(funcToTest4):
    res = funcToTest4
    assert(res == "Будильник установлен на: " + datetime.now().strftime("%H:%M"))

def test_showMessage_Incorrect(funcToTest5):
    res = funcToTest5
    assert(res == "Некорректный ввод данных")

