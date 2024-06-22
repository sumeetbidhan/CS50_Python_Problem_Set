import bank
from bank import value

def test_value():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"
    assert value("HELLO") == "$0"
    assert value("hey") == "$20"
    assert value("Hey") == "$20"
    assert value("hi") == "$20"
    assert value("Hi") == "$20"
    assert value("hola") == "$20"
    assert value("Hola") == "$20"
    assert value("what's up") == "$100"
    assert value("Greetings") == "$100"
    assert value("Hello there") == "$0"  
    assert value("  Hello") == "$0"
    assert value("hey!") == "$20"
    assert value(" H ") == "$20"

