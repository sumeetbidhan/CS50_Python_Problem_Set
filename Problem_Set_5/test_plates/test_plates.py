import plates
from plates import is_valid

def test_is_valid():
    assert is_valid("ASD123") == True
    assert is_valid("AS") == True
    assert is_valid("A1") == False
    assert is_valid("12345") == False
    assert is_valid("A") == False
    assert is_valid("ASD1234") == False
    assert is_valid("ASD12D") == False
    assert is_valid("ASD 123") == False
    assert is_valid("ASD1230") == False
    assert is_valid("01230") == False
    assert is_valid("A&@#0") == False
