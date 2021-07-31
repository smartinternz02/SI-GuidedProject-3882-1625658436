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
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
