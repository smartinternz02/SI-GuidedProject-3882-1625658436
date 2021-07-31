import wiotp.sdk.device
import time
import random
myConfig = {
    "identity": {
        "orgId": "96dm08",
        "typeID": "A4",
        "deviceId": "12321"
    },
    "auth": {
        "token": "JivikaS@4"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])

client = wiotp.sdk.device.DeviceClient(config = myConfig, logHandlers=None)
client.connect()

while True:
    wlevel=random.randit(0,100)
    light=random.randint(0,100)
    myData={'Water_Level':wlevel, 'Light_Intensity':light}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
print("Published data Successfully: %s", myData)
    client.commandCallback = myCOmmandCallback
    time.sleep(2)
client.disconnect()

