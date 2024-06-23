import pytest
from seasons import validate, calculate_minutes, convert_minutes
from datetime import date

def test_validate():
    assert validate("1999-01-01") == date(1999, 1, 1)
    assert validate("2020-02-29") == date(2020, 2, 29)
    with pytest.raises(ValueError):
        validate("2021-13-01")
    with pytest.raises(ValueError):
        validate("not-a-date")

def test_calculate_minutes():
    birthdate = date(2000, 1, 1)
    today = date.today()
    delta = today - birthdate
    expected_minutes = delta.days * 24 * 60
    assert calculate_minutes(birthdate) == expected_minutes

def test_convert_minutes():
    assert convert_minutes(525600) == "five hundred twenty-five thousand six hundred"
    assert convert_minutes(1051200) == "one million fifty-one thousand two hundred"
    assert convert_minutes(2629440) == "two million six hundred twenty-nine thousand four hundred forty"
    assert convert_minutes(6092640) == "six million ninety-two thousand six hundred forty"
    assert convert_minutes(806400) == "eight hundred six thousand four hundred"

if __name__ == "__main__":
    pytest.main()
