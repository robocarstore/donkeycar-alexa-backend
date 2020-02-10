import requests

# defining the api-endpoint
API_ENDPOINT = "http://alexa.proactivesystem.com.hk/command"
API_ENDPOINT = "http://localhost:5000"



# # defining the api-endpoint
# API_ENDPOINT = "http://alexa.proactivesystem.com.hk/pair_id/{}".format("12345")

# # sending post request and saving response as response object
# r = requests.get(url = API_ENDPOINT, json = data)

# print(r.pairId)

def test_post_command():
    # data to be sent to api
    url = "{}/{}".format(API_ENDPOINT, 'command')
    data = {
        'command': 'autopilot',
        'deviceId': 'device123'
    }

    # sending post request and saving response as response object
    r = requests.post(url = url, json = data)
    rData = r.json()

    assert rData['statusCode'] == 200

def test_get_device_code():
    deviceId = 'device123'
    url = "{}/{}/{}".format(API_ENDPOINT, 'device_code', deviceId)

    r = requests.get(url = url)
    rData = r.json()
    assert rData['deviceCode'] == '52523716'


def test_get_command():
    deviceCode = '52523716'
    url = "{}/{}".format(API_ENDPOINT, 'command')

    params = {
        'deviceCode': deviceCode
    }

    r = requests.get(url = url, params= params)
    rData = r.json()
    assert rData['statusCode'] == 200
    assert rData['command'] == 'autopilot'


def test_get_command_new_device_code():
    deviceCode = '12345678'
    url = "{}/{}".format(API_ENDPOINT, 'command')

    params = {
        'deviceCode': deviceCode
    }

    r = requests.get(url = url, params= params)
    rData = r.json()
    assert rData['command'] == None

def test_get_command_empty_device_code():
    url = "{}/{}".format(API_ENDPOINT, 'command')

    r = requests.get(url = url)
    rData = r.json()
    assert rData['statusCode'] == 500









