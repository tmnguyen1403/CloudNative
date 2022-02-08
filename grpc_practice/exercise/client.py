import grpc
import order_pb2
import order_pb2_grpc


print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
item = order_pb2.OrderMessage(
    id="Pan",
    created_by="Amazon",
    status= order_pb2.OrderMessage.Status.QUEUED,
    created_at="10:00PM",
    equipment=[
        order_pb2.OrderMessage.Equipment.KEYBOARD,
        order_pb2.OrderMessage.Equipment.MOUSE
    ]
)

response = stub.Create(item)
print(response)