import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc

class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):
        print("receive create order request")
        #getting equipment
        request_value = {
            "id": request.id,
            "created_by": request.created_by,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": request.equipment
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)
    def Get(self, request, context):
        print("received request retrieving orders")
        result = order_pb2.OrderMessageList()
        order1 = order_pb2.OrderMessage(
            id="111",
            created_by="user1",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2022-01-01',
            equipment=[order_pb2.OrderMessage.Equipment.MOUSE]
        )
        result.orders.extend([order1])
        return result

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)

print("server starting on port 5005...")
server.add_insecure_port("[::]:5005")
if __name__ == "__main__":
    server.start()
    # Keep thread alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

