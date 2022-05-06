from umqttsimple import MQTTClient
import machine,utime,time,network
import gc
mq_server = 'test.mosquitto.org'  #A test server provided by Mosquitto.org
mq_id = 'ESPDevice' 
mq_topic = 'Topic'    #Change topic to unique names to have a clear channel.
mq_user= None
mq_pass= None
gc.collect()

def sub_cb(topic, msg):
  print((topic, msg))

def connect_and_subscribe():
  global mq_id, mq_server, mq_topic
  client = MQTTClient(mq_id, mq_server, user=mq_user, password=mq_pass, port=1883, keepalive=60)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(mq_topic)
  return client

while True:
    client.check_msg()
    time.sleep(2)
