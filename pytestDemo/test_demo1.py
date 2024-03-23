# any pytest file should start with test_
# pytest method names should start with test
# py.test -v -s
# py.test test_demo2.py -v -s
# py.test -k "common keyword of method name" -v -s
# -k stands for method names executions, -s stands for logs in output, -v stands for more info meta data
# py.test -m smoke -v -s >> grouping
#A fixture can be used to set up preconditions for a test, provide data, or perform a teardown after a test is finished. They are defined using the @pytest.

import pytest

@pytest.mark.skip
@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.skip
def test_secondProgram_check():
    msg = "Sun"
    assert msg == "Moon", "Result does not match"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)


