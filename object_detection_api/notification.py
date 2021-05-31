import requests
import os
import pycurl
from io import StringIO
import json

FCM_URL = 'your-fcm-url'
AUTH_KEY = 'your-auth-key'
DEVICE_KEY = "your-device-key"

def curl_command_line(notif_data):
    data = {
        "to": DEVICE_KEY,
        "data": notif_data
    }

    command = 'curl -X POST -H "Authorization: {} -H "Content-Type: application/json" -d "{}" {}'.format(AUTH_KEY, data, FCM_URL)
    print(command)
    os.system(command)

def python_request(notif_data):
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    data = {
        "to": DEVICE_KEY,
        "data": notif_data
    }

    response = requests.post(FCM_URL, headers=headers, data=data)
    print(response.status_code)

def python_pycurl(notif_data):
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, FCM_URL)

    header = ['Authorization: {}'.format(AUTH_KEY), 'Content-Type: application/json']
    curl.setopt(pycurl.HTTPHEADER, header)
    curl.setopt(pycurl.POST, 1)

    # If you want to set a total timeout, say, 3 seconds
    curl.setopt(pycurl.TIMEOUT_MS, 3000)

    ## depending on whether you want to print details on stdout, uncomment either
    curl.setopt(pycurl.VERBOSE, 1) # to print entire request flow
    ## or
    # curl.setopt(pycurl.WRITEFUNCTION, lambda x: None) # to keep stdout clean

    # preparing body the way pycurl.READDATA wants it
    # NOTE: you may reuse curl object setup at this point
    #  if sending POST repeatedly to the url. It will reuse
    #  the connection.
    data = {
        "to": DEVICE_KEY,
        "data": notif_data
    }

    body_as_json_string = json.dumps(data) # dict to json
    body_as_file_object = StringIO(body_as_json_string)

    # prepare and send. See also: pycurl.READFUNCTION to pass function instead
    curl.setopt(pycurl.READDATA, body_as_file_object) 
    curl.setopt(pycurl.POSTFIELDSIZE, len(body_as_json_string))
    curl.perform()

    # you may want to check HTTP response code, e.g.
    status_code = curl.getinfo(pycurl.RESPONSE_CODE)
    if status_code != 200:
        print("Aww Snap :( Server returned HTTP status code {}".format(status_code))

    # don't forget to release connection when finished
    curl.close()