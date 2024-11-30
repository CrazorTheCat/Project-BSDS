from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import ClubDatabaseHandler
from Classes.Stream.StreamEntryFactory import StreamEntryFactory
import json

class AllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(len(fields["StreamData"]))
        for i in fields["StreamData"]:
            self.writeVInt(i['StreamType'])
            StreamEntryFactory.encode(self, fields, i)

    def decode(self):
        fields = {}
        fields["StreamCount"] = self.readVInt()
        fields["Streams"] = []
        for i in range(fields["StreamCount"]):
            fields["Streams"].append({"StreamType": self.readVInt(), "StreamData": None}) # wont work as its not completed
        return {}

    def getMessageType(self):
        return 24311

    def getMessageVersion(self):
        return self.messageVersion