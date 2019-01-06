import paho.mqtt.client as mqtt , os, urlparse
import time
import ssl

# Define event callbacks
def on_connect(mosq, obj, flags, rc):
    print ('on_connect:: Connected with result code '+ str ( rc ) )
    print('rc: ' + str(rc))

def on_message(mosq, obj, msg):
    print ('on_message:: this means  I got a message from broker for this topic')
    print(msg.topic + ' ' + str(msg.qos) + ' ' + str(msg.payload))
    if ( msg.payload == 'on' ):
    	print ('Lights on')
    else :
    	print ('Lights off')
		
def on_subscribe(mosq, obj, mid, granted_qos):
    print('This means broker has acknowledged my subscribe request')
    print('Subscribed: ' + str(mid) + ' ' + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

client = mqtt.Client()
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

# Uncomment to enable debug messages
client.on_log = on_log


#Connect to the Broker
client.tls_set(ca_certs='all-ca.crt', certfile='mqttclient.crt',
                            keyfile='mqttclient.key', cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.connect('mqttserver', 8883, 60)

client.loop_start()         #start the loop

#Subscribe to messages
client.subscribe ('/IoTSensor/Sensor01',0)

try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print ('exiting')
    client.disconnect()
    client.loop_stop()
