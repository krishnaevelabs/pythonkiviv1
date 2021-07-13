class button:
    id = ""
    status = ""
    callStatus = ""
    cardStatus = ""
    bedName = ""
    location = ""
    batteryPercent = ""
    sendAck = ""

    def __init__(self, id, bedName, location):
        self.id = id
        self.bedName = bedName
        self.location = location
        self.sendAck = "ack"
        self.status = "offline"

    def call(self, callStatus, cardStatus, batteryPercent):
        self.callStatus = callStatus
        self.status = "online"
        self.cardStatus = cardStatus
        self.batteryPercent = batteryPercent

    def frontendAck(self, sendAck):
        self.sendAck = sendAck

    def cancel(self):
        self.sendAck = "ack"
        self.status = "offline"

    def ack(self):
        self.sendAck = "ack"
        self.status = "offline"
