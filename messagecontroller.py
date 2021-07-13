# Parse the raw message recieved in serial input
def deviceIdentifier(rawMessage):
    # call this function and identify the device
    return 0


def nurseMessageParser(rawMessage):
    try:
        parsedMessage = rawMessage.split("-")

        parsedDeviceId = parsedMessage[0].split(">")
        id = parsedDeviceId[1]
        callStatus = parsedMessage[2]
        attend_id = parsedMessage[4]
        batteryPercent = parsedMessage[5]
        return [id, callStatus, attend_id, batteryPercent]
    except:
        return None

# def nurseCallAction(id,callStatus,batteryPercent):
#     for item in buttons:
#         if item.id==id:
#             print(item.status)
#         else:
#             print("Device not Authenticated")
