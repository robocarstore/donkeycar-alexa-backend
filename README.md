# Introduction
This is a simple backend to catch commands coming from Alexa. It acts as a temp storage place until the donkey car poll the command.

It supports multiple alexa sending commands to different donkey car. You will need to find out the device id of the alexa and put the device id to the donkey car so that they could be linked.

# How to run
```
docker-compose up
```

# Set a command
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"command": "super"}' \
  localhost:5000/command/alexa_device_id
```