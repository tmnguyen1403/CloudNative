import grpc
import item_pb2
import item_pb2_grpc


print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = item_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
item = item_pb2.ItemMessage(
    name="Pan",
    brand_name="Amazon",
    id=4,
    weight=4.5
)

response = stub.Create(item)
