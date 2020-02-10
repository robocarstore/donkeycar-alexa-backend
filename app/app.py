from flask import Flask, escape, request
import uuid, logging

app = Flask(__name__)

commands = dict()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/command/<userid>', methods=['GET', 'POST'])
def command(userid):

    if request.method == 'POST':
        commands[userid] = request.json['command']

        return {
            "statusCode": 200,
            "userid": "userid"
        }
    elif request.method == 'GET':
        result = {
            "statusCode": 200,
            "userid": "userid",
            "command": commands.pop(userid, None)
        }
        return result