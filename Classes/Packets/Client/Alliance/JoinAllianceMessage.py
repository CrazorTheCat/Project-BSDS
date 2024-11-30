from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class JoinAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AllianceID"] = self.readLong()
        super().decode(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        fields["Socket"] = calling_instance.client
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])

        if len(clubData["Members"]) < 100:
            playerData = db_instance.getPlayer(calling_instance.player.ID)
            lastMessageID = clubData['ChatData'][-1]['StreamID'][1] + 1 if clubData["ChatData"] else 1
            clubData['Members'].append(clubdb_instance.getDefaultMembersData(calling_instance.player, 1))
            joinStreamData = clubdb_instance.getDefaultMessageData(4, 3, [0, lastMessageID],
                                                          calling_instance.player.ID, calling_instance.player.Name,
                                                          1,
                                                          )
            if joinStreamData not in clubData['ChatData']: clubData['ChatData'].append(joinStreamData)
            clubdb_instance.updateClubData(clubData, clubData['LowID'])
            playerData["AllianceID"] = [clubData["HighID"], clubData["LowID"]]
            db_instance.updatePlayerData(playerData, calling_instance)
            calling_instance.player.AllianceID = playerData["AllianceID"] # It's better than loading the account again!
            fields["ResponseID"] = 40
            Messaging.sendMessage(24333, fields)
            fields.clear()
            fields["Socket"] = calling_instance.client
            fields["HasClub"] = True
            Messaging.sendMessage(24399, fields, calling_instance.player)
            fields.clear()
            fields["Socket"] = calling_instance.client
            Messaging.sendMessage(24311, fields, playerIDs=clubData["Members"], item="LowID")
            fields["AllianceID"] = calling_instance.player.AllianceID
            Messaging.sendMessage(24301, fields, playerIDs=clubData["Members"], item="LowID")
        else:
            fields["ResponseID"] = 42
            Messaging.sendMessage(24333, fields)

        db_instance.cursor.close()
        clubdb_instance.cursor.close()

    def getMessageType(self):
        return 14305

    def getMessageVersion(self):
        return self.messageVersion