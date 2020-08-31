from kafka import KafkaConsumer
from json import loads
from time import sleep

print("Starting Consumer")


def forgiving_json_deserializer(v):
    if v is None:
        return None
    try:
        return json.loads(v.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        return None 

def main():

    # consumer = KafkaConsumer(
    # 't1',
    #  bootstrap_servers=['192.168.5.191:9092'],
    #  auto_offset_reset='earliest',
    #  enable_auto_commit=True,
    #  group_id='my-group',
    #  #value_deserializer=forgiving_json_deserializer
    #  value_deserializer= lambda m: loads(m.decoder('utf-8'))
    #  )


    consumer = KafkaConsumer('t1', bootstrap_servers=['192.168.5.191:9092'])

    for msg in consumer:
        if msg is not None:
            message = msg.value
            print("Received: {}".format(message))


if __name__ == "__main__":
    main()

# consumer = KafkaConsumer(
#     't1',
#      bootstrap_servers=['192.168.5.191:9092'],
#      auto_offset_reset='earliest',
#      enable_auto_commit=True,
#      group_id='1001',
#      value_deserializer=lambda x: loads(x.decode('utf-8')))
# # consumer.subscribe(['msgpackfoo'])
# for message in consumer:
#     message = message.value
#     print(message)