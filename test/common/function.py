"""Functions for testing handlers"""

import requests
import json

from test.common.config import variables


def get_purchase(data, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    r = requests.get(variables.get("host") + 'v1/item/purchase/by-client', data=json.dumps(data), headers=headers)
    j = json.loads(r.text)
    return j


def create_client(data, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    r = requests.post(variables.get("host") + 'v1/client/create', data=json.dumps(data), headers=headers)
    j = json.loads(r.text)
    return j


def create_order(data, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    r = requests.post(variables.get("host") + 'v1/order/create', data=json.dumps(data), headers=headers)
    j = json.loads(r.text)
    return j
