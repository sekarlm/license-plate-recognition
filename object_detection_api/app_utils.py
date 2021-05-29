import requests

def post_to_android(url, send_data):
    headers = {
        'Authorization': 'key=AAAAqwEcUuY:APA91bG_UTv4R0QS4lvGcKSdsCOa2Rd0rZQci03nRHa9FgN9u3us8bupo2DWNzXmCLqqHo-pa-XjYjzlMPQI-lQug-mNKKWeOn70niTAGqPYAH2YySrV3FCzJgkNppbTUOK2W40ar6Mp',
        'Content-Type': 'application/json',
    }

    data = { 
        "to" : "d5CBabd-Tg2m3DG5Kt55qc:APA91bHxSOsT6aWcjON8rH5qHxPfqgxmPxzYU-TdyO8yhRJM71cunYyPjvPIelG8gBPjbpoAwGazA6wuT4H0ryiQYBTTrLUnucjfCHG7xaoqoO3jROkj3-njzZ6cDlJsCBobmuY_r3dh", 
        "priority" : "high", 
        "data" : send_data
    }

    response = requests.post(url, headers=headers, data=data)