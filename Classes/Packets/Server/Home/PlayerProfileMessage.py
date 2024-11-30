import json

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.PlayerProfile import PlayerProfile
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry

class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(fields["PlayerID"])

        PlayerProfile.encode(self, fields, playerData)

        self.writeBoolean(playerData["AllianceID"] != [0, 0])
        if playerData["AllianceID"] != [0, 0]:
            clubdb_instance = ClubDatabaseHandler()
            clubData = json.loads(clubdb_instance.getClubWithLowID(playerData["AllianceID"][1])[0][1])
            memData = clubdb_instance.getMemberWithID(clubData, playerData["ID"])
            AllianceHeaderEntry.encode(self, clubdb_instance, clubData)
            self.writeDataReference(25, memData["Role"])
        else:
            self.writeDataReference(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion