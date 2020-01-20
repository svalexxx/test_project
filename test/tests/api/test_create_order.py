"""Tests for create_order handler"""

from parametrization import Parametrization

from test.common.generators import *
from test.common.function import create_order
from service.src import res


class TestCreateOrder:
    def test_positive(self):
        data = {
            "client_id": "1",
            "address": fake_address(),
            "phone": fake_phone_number(),
            "items": [
                        {
                            "item_id": "1",
                            "price": 1.5,
                            "quantity": 1
                        }
                    ]
        }
        r = create_order(data)
        assert r is not None
