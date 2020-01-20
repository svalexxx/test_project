"""Get Purchase"""

from parametrization import Parametrization

from test.common.generators import *
from test.common.function import get_purchase
from service.src import res


class TestGetPurchase:
    def test_positive(self):
        data = {
            "client_id": "1",
            "item_ids": ["1"]
        }
        r = get_purchase(data)
        assert r["items"] is not None

    @Parametrization.parameters("client_id", "items_ids", "response")
    @Parametrization.case("client_id_is_none", None, ["1"], res.error_response)
    @Parametrization.case("items_ids_is_none", "1", None, res.error_response)
    @Parametrization.case("client_id_digit", int(digits_string(3)), ["1"], res.error_response)
    def test_negative(self, client_id, items_ids, response):
        data = {
            "client_id": client_id,
            "item_ids": items_ids
        }
        r = get_purchase(data)
        assert r == response
