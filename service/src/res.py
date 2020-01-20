"""Examples of response"""

get_purchase_response = {
   "items": [
      {
         "item_id": "1",
         "purchased": "is_purchased",
         "last_order_number": "1",
         "last_purchase_date": "2020-01-16T13:33:00.000Z",
         "purchase_count": "1"
      }
   ]
}

create_order_response = {
   "order_id": "1",
   "order_number": "Order №1"
}

create_client_response = {
   "client_id": "1"
}

error_response = {
    "error": "error message"
}
