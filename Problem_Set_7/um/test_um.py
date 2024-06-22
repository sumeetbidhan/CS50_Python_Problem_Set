from um import count

def test_single_um():
    assert count("um") == 1

def test_um_with_punctuation():
    assert count("um, thanks") == 1

def test_multiple_ums():
    assert count("um, um...") == 2

def test_um_as_substring():
    assert count("yummy") == 0

def test_um_case_insensitive():
    assert count("Um, thanks") == 1
    assert count("UM") == 1

def test_um_with_other_text():
    assert count("hello, um, world") == 1
    assert count("Um, thanks for the album.") == 1
