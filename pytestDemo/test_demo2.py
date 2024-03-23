import pytest


def test_greet():
    print("Nice to meet you!")

def test_greet_new():
    print("Hello, Nice to meet you!")


@pytest.mark.smoke
def test_check():
    a = 7
    b = 2

    assert b + 5 == 6, "Addition do not match"


    