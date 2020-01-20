"""Conftest file for API testing"""

import pytest

from test.common.function import create_client
from test.common.generators import *


@pytest.fixture(scope="class")
def create_client_fixture():
    client_id = create_new_client()
    yield str(client_id)


def create_new_client():
    data = {
        "name": fake_name(),
        "surname": fake_surname(),
        "phone": fake_phone_number()
    }
    r = create_client(data)
    return r["client_id"]
