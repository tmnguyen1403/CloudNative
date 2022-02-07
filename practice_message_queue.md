Your company wants to invest more in the computer ordering service! The tool is very popular and usage is expected to grow. On top of that, they want to build out a tool that enables customers to track the status of the computers as it goes through the fulfillment process. The fulfillment process involves an order being placed, registered, acknowledged, processed, and shipped. The company will be using various sensors to track where the computer order is in the fulfillment process -- you simply need to worry about providing an interface for this data to land.

Leverage message queues to show how they can be used to handle the increasing requests from customers and how the computer order tracking system can be used

How Can a Message Queue Alleviate the Increased API Load?
Kafka is very useful for handling large volumes of data -- especially data that comes in as events. We will be expecting a large stream of events as they come in from our service. This will help prevent our server from crashing due to load but our messages will be backlogged as we won’t be able to process them more quickly.

How Can a Distributed Message Broker Help?
Databases are designed for specific use cases and often not optimized to function as a message broker. Using a queue should require high write performance. MySQL will lock table rows and prevent more than one resource from updating a row at a time. This can cause delays and even issues for data entering our makeshift queue. This implementation will also require a lot of custom logic to reshape the database into a queue..
