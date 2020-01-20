from flask import Flask, request, abort, Response, Request
from datetime import datetime
from jsonschema import validate, ValidationError

from service.src import req, res

app = Flask(__name__)


@app.route('/v1/client/create', methods=['POST'])
def create_client():
    if request.method == 'POST':
        print(request.json)
        try:
            validate(request.json, req.create_client_request)
            return res.create_client_response, 200
        except ValidationError:
            return res.error_response, 400
    else:
        return res.error_response, 400


@app.route('/v1/order/create', methods=['POST'])
def create_order():
    if request.method == 'POST':
        print(request.json)
        try:
            validate(request.json, req.create_order_request)
            return res.create_order_response, 200
        except ValidationError:
            return res.error_response, 400
    else:
        return res.error_response, 400


@app.route('/v1/item/purchase/by-client', methods=['GET'])
def get_purchase():
    if request.method == 'GET':
        print(request.json)
        try:
            validate(request.json, req.get_purchase_request)
            return res.get_purchase_response, 200
        except ValidationError:
            return res.error_response, 400
    else:
        return res.error_response, 400


if __name__ == '__main__':
    app.run(host='localhost', port=5555, debug=True)
