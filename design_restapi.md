## Computer Order
-- When a user orders a computer, we want to allow users to specify equipment such as
a keyboard or a webcam to include with the order
-- An order should contain information on the user who created the order, status of 
the order, the time the order was place, and additional equipment.

1. Create an API endpoint for placing an order for a computer:
inclue the request headers, request body, and request URL, response code,
and response body.
-- Request
POST /orders/computers
{
 user: <user_id:string>,
 equipments: 
 {
  <name: string>
 }
}
-- Response
Status code 201 - Created
{
 order_id: <string>,
 status: <string>
}

2. Create an API endpoint for retrieving a list of all computer orders that have been place:
include the request headers, request body, request URL, response code, and response body.
--Request
GET /orders/computers

--Response
Status code 200 - OK
{
 order_ids: 
 {
  <id:string>
 }
}
## Solution
1. Order a computer
-- Request
POST <BASE_URL>/api/orders/computers
Content-Type: application/json
{
  "order_id": <order_id: str>,
  "created_by": <user_id: str>,
  "status": <status_enum: str>,
  "created_at": <isoformat_timestamp: str>,
  "equipment": [
    <equipment: str>
  ]
}
-- Response
201 Created
{
 "computer_orders": [
 	{
  		"order_id": <order_id: str>,
  		"created_by": <user_id: str>,
  		"status": <status_enum: str>,
  		"created_at": <isoformat_timestamp: str>,
  		"equipment": [
    		<equipment: str>
  		]
	}
 ]
}
2. Retrieve order
-- Request
GET <BASE_URL>/api/orders/computers
-- Response
200 OK
{
 "computer_orders": [
 	{
  		"order_id": <order_id: str>,
  		"created_by": <user_id: str>,
  		"status": <status_enum: str>,
  		"created_at": <isoformat_timestamp: str>,
  		"equipment": [
    		<equipment: str>
  		]
	}
 ]
}
