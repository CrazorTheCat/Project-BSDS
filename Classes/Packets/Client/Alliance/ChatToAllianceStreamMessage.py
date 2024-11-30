import json

from Classes.Messaging import Messaging
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import ClubDatabaseHandler

class ChatToAllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def decode(self):
        fields = {"Message": self.readString()}
        return fields

    def execute(message, calling_instance, fields):
        clubdb_instance = ClubDatabaseHandler()
        fields["Socket"] = calling_instance.client
        fields["AllianceID"] = calling_instance.player.AllianceID
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])
        memberData = clubdb_instance.getMemberWithID(clubData, calling_instance.player.ID)
        fields["Socket"] = calling_instance.client
        lastMessageID = clubData['ChatData'][-1]['StreamID'][1] + 1 if clubData["ChatData"] else 1
        streamData = clubdb_instance.getDefaultMessageData(2, 0, [0, lastMessageID],
                                                               calling_instance.player.ID, calling_instance.player.Name,
                                                               memberData["Role"],
                                                               msgData=fields["Message"]
                                                               )
        fields["StreamData"] = [streamData]
        clubData["ChatData"].append(streamData)
        clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
        Messaging.sendMessage(24311, fields, playerIDs=clubData["Members"], item="LowID")

    def getMessageType(self):
        return 14315

    def getMessageVersion(self):
        return self.messageVersion