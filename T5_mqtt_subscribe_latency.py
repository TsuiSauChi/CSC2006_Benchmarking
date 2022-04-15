import paho.mqtt.client as mqtt 
import paho.mqtt.publish as publish
import time

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    print()
    print("Topic", msg.topic)
    print("Payload", msg.payload.decode("utf8"))

def Average(lst):
    return sum(lst) / len(lst)

### Define the MQTT Endpoint
client.username_pw_set("testsauchi@ttn", "NNSXS.VHLPH6BUMFKLCBTGAGEWXGPHJBH5YOWQ3OMAJ5Q.FBLAYZHHKTNU37QLAD3QWH4TBQ3OOOYQUAM3HSRLW5RYMT6A3EDA")
client.connect("au1.cloud.thethings.network", 1883)
client.on_connect = on_connect

time_list = []

### Publishers and listen to subscribe
### Calculate RTT 
for i in range(10):
    print("COUNTER: ", i)
    start_time = time.time()
    publish.single("v3/testsauchi@ttn/devices/eui-70b3d57ed004f58b/down/push",'{"downlinks":[{"f_port": 1,"frm_payload":"vu8=","priority": "NORMAL"}]}',qos=0, retain=False, hostname="au1.cloud.thethings.network",  port=1883, auth={'username':"testsauchi@ttn",'password':"NNSXS.VHLPH6BUMFKLCBTGAGEWXGPHJBH5YOWQ3OMAJ5Q.FBLAYZHHKTNU37QLAD3QWH4TBQ3OOOYQUAM3HSRLW5RYMT6A3EDA"})
    client.on_message = on_message
    time_list.append(time.time() - start_time)

# Calculate the average time
average = Average(time_list)

# Printing average of the list
print("Average RRT =", average, "s")
print("Average Time for One Directional Latency", average/2, "s")

client.loop_forever()