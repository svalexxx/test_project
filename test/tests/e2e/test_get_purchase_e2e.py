"""E2E test for get_purchase handler"""

from test.common.function import create_client, create_order, get_purchase
from test.common.generators import *


class TestGetPurchaseE2E:
    def test_create_new_client(self):
        global client_id
        data = {
            "name": fake_name(),
            "surname": fake_surname(),
            "phone": fake_phone_number()
        }
        r = create_client(data)
        assert r is not None
        client_id = r["client_id"]

    def test_create_new_order(self):
        global order_id
        data = {
            "client_id": str(client_id),
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
        order_id = r["order_id"]

    def test_get_purchase_by_client(self):
        data = {
            "client_id": str(client_id),
            "item_ids": ["1"]
        }
        r = get_purchase(data)
        assert r is not None
        assert str(order_id) == r["items"][0]["last_order_number"]
