import ssl
import paho.mqtt.client as mqtt
import ast


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed", client, userdata, mid, granted_qos)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    print(f"Message received: {message.payload}")
    jsonString = message.payload
    dict_str = jsonString.decode("UTF-8")
    global jsonData
    jsonData = ast.literal_eval(dict_str)
    file1 = open("var.txt", "w+")
    file1.write(str(jsonData))


broker_address = "mqtt.cloud.yandex.net"
port = 8883
user = "aresmv64htqk8lkmqr61"
password = "ICLinnocamp2022"


client = mqtt.Client("kazanka")
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.tls_set(r"rootCA.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)
client.connect(broker_address, port=port)
client.subscribe("$devices/are9gnqohp4npug37mbs/events/raw")


client.loop_forever()





