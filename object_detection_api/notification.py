import requests
import os
import pycurl
from io import StringIO
import json
import sys

FCM_URL = 'https://fcm.googleapis.com/fcm/send'
AUTH_KEY = 'key=AAAAqwEcUuY:APA91bG_UTv4R0QS4lvGcKSdsCOa2Rd0rZQci03nRHa9FgN9u3us8bupo2DWNzXmCLqqHo-pa-XjYjzlMPQI-lQug-mNKKWeOn70niTAGqPYAH2YySrV3FCzJgkNppbTUOK2W40ar6Mp'
DEVICE_KEY = 'etk7hgw9Q9OxuMbh3qNezw:APA91bEcwEMEc-839HwY5NMXPm_w_sXE--LULRL4uxKq1gUlMvmtOl_SGZQrxxNdAeelYhC50JjB-lcI_YO3bH-KV9MtzzzFcREmd-YT1j3vVjOrkvelKlRdL0YNqkqeGFnNNoM3l2Od'

def send_notification(notif_data):
    
    command = 'curl -X POST -H "Authorization: {}" -H "Content-Type: application/json" -d \'{}\' {}'.format(AUTH_KEY, notif_data, FCM_URL)
    print(command)
    os.system(command)

# testing code
if __name__ == '__main__':
    mode = sys.argv[1]

    time_enter = "02:09:430"
    time_out = "03:39:450"
    duration = "24h 45m 450s"
    place = "Rumah Anna"
    price = "Rp 35.000.000"

    notif_data = json.dumps({
        "to" : "{}".format(DEVICE_KEY),
        "data" : {
        "body": "Please pay the parking fare!",
        "title":"You are going out",
        "timein": time_enter,
        "timeout": time_out,
        "totaltime": duration,
        "fare": price,
        "location": place
        },
        "notification": {
        "body": "Please pay the parking fare!",
        "title": "You are going out",
        "click_action": "com.dicoding.nextparking.ui.payment.PaymentActivity"
        }
        })

    if mode == 'command-line':
        send_notification(notif_data)
    else:
        print("wrong argument")