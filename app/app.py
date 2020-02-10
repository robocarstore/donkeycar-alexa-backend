from flask import Flask, escape, request
import uuid, logging
import hashlib

app = Flask(__name__)



# A mapping between pairing id and latest command
commands = dict()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/command', methods=['GET', 'POST'])
def command():
    if request.method == 'POST':
        # Alexa sending command to us
        deviceId = request.json['deviceId']
        deviceCode = getDeviceCodeByDeviceId(deviceId)

        commands[deviceCode] = request.json['command']

        return {
            "statusCode": 200
        }
    elif request.method == 'GET':
        deviceCode = request.args.get('deviceCode')

        if deviceCode is not None:
            result = {
                "statusCode": 200,
                "command": commands.pop(deviceCode, None)
            }
        else:
            result = {
                "statusCode": 500
            }
        return result


# This endpoint simply an Alexa device id (normally very long) to a numeric string (max 6 digits) which is easier to pass along
@app.route('/device_code/<deviceId>', methods=['GET'])
def device_code(deviceId):
    deviceCode = getDeviceCodeByDeviceId(deviceId)
    return {
        "deviceCode": deviceCode
    }

def getDeviceCodeByDeviceId(deviceId):
    # https://stackoverflow.com/questions/16008670/how-to-hash-a-string-into-8-digits
    deviceCode = int(hashlib.sha256(deviceId.encode('utf-8')).hexdigest(), 16) % 10**6
    return str(deviceCode)
