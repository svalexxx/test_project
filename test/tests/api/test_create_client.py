"""Create client"""

from parametrization import Parametrization

from test.common.generators import *
from test.common.function import create_client
from service.src import res


class TestCreateClient:
    def test_positive(self):
        data = {
            "name": fake_name(),
            "surname": fake_surname(),
            "phone": fake_phone_number()
        }
        r = create_client(data)
        assert r is not None
