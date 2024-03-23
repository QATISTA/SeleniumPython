import pytest


@pytest.fixture()
# @pytest.fixture(scope='class')  # The fixture will be call at the beggining of the program and yeild will be called at the end of the program
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("User Profile is being created")
    return ["Rahul","Shetty","rahul1@yopmail.com"]

@pytest.fixture(params=[("Chrome","Rahul"),("Firefox","Shetty"),("IE","Rohan")])
def crossBrowser(request):
    return request.param