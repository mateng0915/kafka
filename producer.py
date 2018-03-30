from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
import sys
import requests
import time

def get_data():
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=USD"
    DATA = requests.request("GET", url)
    print(DATA.text)
    return DATA

if __name__ == '__main__':
	kafka = KafkaClient('127.0.0.1:9092')
	producer = KafkaProducer()

	group_name = "my-group"
	topic_name = "fast-messages"
	print "sending messages to group: [%s] and topic: [%s]" % (group_name, topic_name)
	
	while True:
		message = get_data()
		time.sleep(10)
		producer.send('fast-messages', value='DATA')





