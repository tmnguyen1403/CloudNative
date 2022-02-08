## Use cases
-- Special type of message queue that is often used to handle large volumes of data generated continously as events
-- application logs & user activity
-- distributed system
-- when a producer writes data to Kafka, it stores the data inside of topics
-- topics are abstraction of Kafka where messages can be stored and referenced
-- internally, topics are distributed as partitions in different nodes and allow parallelized operations
https://kafka.apache.org/quickstart
After download Kafka

## Create topic
-- Navigating into kafka folder
$ bin/kafka-topics.sh --create --topic items --bootstrap-server localhost:9092  

## Read events
$ bin/kafka-console-consumer.sh --topic items --from-beginning --bootstrap-server localhost:9092

## Write events
$ bin/kafka-console-producer.sh --topic items --bootstrap-server localhost:9092

$
## Kafka Python
$ pip install kafka-python
$
## References
https://www.cloudkarafka.com/blog/cloudkarafka-what-is-zookeeper.html
https://www.confluent.io/blog/removing-zookeeper-dependency-in-kafka/
https://www.confluent.io/blog/how-kafka-is-used-by-netflix/
