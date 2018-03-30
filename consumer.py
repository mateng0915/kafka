from kafka import SimpleConsumer, SimpleClient
from kafka import KafkaConsumer
from kafka import KafkaClient

group_name = "my-group"
topic_name = "fast-messages"

#kafka = KafkaClient('127.0.0.1:9092')

print("________")
print(topic_name)
print(type(topic_name))
print("________")
consumer = KafkaConsumer(topic_name, group_id=group_name, bootstrap_servers=['127.0.0.1:9092'])

print "Created consumer for group: [%s] and topic: [%s]" % (group_name, topic_name)
print "Waiting for messages..."

for msg in consumer:
    print msg
