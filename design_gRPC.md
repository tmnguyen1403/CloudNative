## Computer Orders
### My solution
syntax = "proto3";
#### Note - the numbers are the field's order
message OrderMessage {
 string id = 1;
 string type = 2;
 string created_by = 3;
 string status = 4;
 string created_date = 5;
 repeated string equipment = 6;
}

Service OrderService {
  rpc Create(OrderMessage) returns (OrderMessage)
  rpc Get() returns (OrderMessage)
}
### Solution - Extra
message OrderMessage {
 enum Status {
    Queued = 0;
    Processing = 1;
    Completed = 2;
    Failed = 3;
  }

  enum Equipment {
    Keyboard = 0;
    Mouse = 1;
    Webcam = 2;
    Monitor = 3;
  }

  string id = 1;
  string created_by = 2;
  Status status = 3 [ default = QUEUED ;
  string created_at = 4;
  repeated Equipment equipment = 5;
}
