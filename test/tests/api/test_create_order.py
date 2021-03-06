"""Tests for create_order handler"""

from test.common.function import create_order
from test.common.generators import *


class TestCreateOrder:
    def test_positive(self, create_client_fixture):
        client_id = create_client_fixture
        data = {
            "client_id": client_id,
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
