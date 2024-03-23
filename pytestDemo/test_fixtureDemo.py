import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("Random code is executed")

    def test_fixtureDemo2(self):
        print("Random code is executed")

    def test_fixtureDemo3(self):
        print("Random code is executed")

    def test_fixtureDemo4(self):
        print("Random code is executed")

    

