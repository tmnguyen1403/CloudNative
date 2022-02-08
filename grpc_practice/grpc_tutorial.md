## Python
$ pip install grpcio-tools

Generate python gRPC files using grpc tools
This command generates two python files that can be imported to use grpc in Python

$ python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ item.proto
## -m grpc_tools.protoc - run python command grpc_tools.protoc
## -I - specify context of the command
