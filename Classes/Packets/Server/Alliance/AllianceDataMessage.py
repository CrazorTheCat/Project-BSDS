from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceFullEntry import AllianceFullEntry
from Database.DatabaseHandler import ClubDatabaseHandler, DatabaseHandler
import json

class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        clubdb_instance = ClubDatabaseHandler()
        db_instance = DatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])

        self.writeBoolean(player.AllianceID == [clubData["HighID"], clubData["LowID"]])
        AllianceFullEntry.encode(self, clubdb_instance, db_instance, clubData)

    def decode(self):
        return AllianceFullEntry.decode(self, None)

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion