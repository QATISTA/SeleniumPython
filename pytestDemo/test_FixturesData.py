import pytest
from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestProfile(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[2])