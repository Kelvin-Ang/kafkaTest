from time import sleep
from json import dumps
from kafka import KafkaProducer


print("Starting Producer")

sleep(20)

producer = KafkaProducer(bootstrap_servers=['192.168.5.191:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e, "bignumber": 100*e}
    producer.send('t1', value=data)
    print("Sent: {}".format(data))
    sleep(5)
