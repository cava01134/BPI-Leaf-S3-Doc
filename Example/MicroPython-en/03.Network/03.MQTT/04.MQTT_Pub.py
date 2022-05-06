from umqttsimple import MQTTClient
import machine,utime,time,network
mq_server = 'test.mosquitto.org'
mq_id = 'ESPDevice' 
mq_topic = 'Unique' #Change topic to a unique name to avoid recieving messages from others.
mq_user= None
mq_pass= None

try:    
    mqClient0 = MQTTClient(mq_id, mq_server, user=mq_user, password=mq_pass,keepalive=30)
    mqClient0.connect()
    i=0
    
    while True:
        mq_message = 'My Message: ' + str(i)
        mqClient0.publish(mq_topic, mq_message)
        time.sleep(2)
        i=i+1
        print("Message published: " + str(i))
except Exception as e: print(e)
