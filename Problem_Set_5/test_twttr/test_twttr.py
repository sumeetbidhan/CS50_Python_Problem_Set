import twttr
from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("12345") == "12345"
    assert shorten("t@witter!") == "t@wttr!"
    assert shorten("Hello, World!") == "Hll, Wrld!"
