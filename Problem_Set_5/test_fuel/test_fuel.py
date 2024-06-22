
from fuel import convert, guage

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1

