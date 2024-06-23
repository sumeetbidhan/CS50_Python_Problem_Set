import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("twelve")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()  # Corrected to create an instance of Jar
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)
