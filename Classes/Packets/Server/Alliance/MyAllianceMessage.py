from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler
import json

class MyAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(0) # Online Members
        self.writeBoolean(fields["HasClub"])

        if fields["HasClub"]:
            clubdb_instance = ClubDatabaseHandler()
            clubData = json.loads(clubdb_instance.getClubWithLowID(player.AllianceID[1])[0][1])
            localMemberData = clubdb_instance.getMemberWithID(clubData, player.ID)

            self.writeDataReference(25, localMemberData["Role"])
        
            AllianceHeaderEntry.encode(self, clubdb_instance, clubData)

            self.writeBoolean(False)

        self.writeBoolean(False) # what is this?

    def decode(self):
        fields = {}
        fields["ResponseID"] = self.readVInt()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24399

    def getMessageVersion(self):
        return self.messageVersion