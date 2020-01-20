create_client_request = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "surname": {
      "type": "string"
    },
    "phone": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "surname",
    "phone"
  ]
}

create_order_request = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "address": {
      "type": "string"
    },
    "phone": {
      "type": "string"
    },
    "items": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "item_id": {
              "type": "string"
            },
            "price": {
              "type": "string"
            },
            "quantity": {
              "type": "string"
            }
          },
          "required": [
            "item_id",
            "price",
            "quantity"
          ]
        }
      ]
    }
  },
  "required": [
    "client_id",
    "address",
    "phone",
    "items"
  ]
}

get_purchase_request = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "item_ids": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    }
  },
  "required": [
    "client_id",
    "item_ids"
  ]
}
