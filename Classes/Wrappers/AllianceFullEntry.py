from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
import json

from Database.DatabaseHandler import ClubDatabaseHandler


class AllianceFullEntry:

    @staticmethod
    def encode(calling_instance, clubdb, db, clubData):
        AllianceHeaderEntry.encode(calling_instance, clubdb, clubData)
        calling_instance.writeString(clubData["Description"])
        
        calling_instance.writeVInt(len(clubData["Members"]))
        for memberData in clubdb.getMembersSorted(clubData):
            playerData = json.loads(db.getPlayerEntry([memberData['HighID'], memberData['LowID']])[2])
            calling_instance.writeLong(memberData['HighID'], memberData['LowID'])
            calling_instance.writeVInt(memberData['Role']) # Role
            calling_instance.writeVInt(playerData['Trophies']) # Trophies
            calling_instance.writeVInt(2) # Player State TODO: Members state
            calling_instance.writeVInt(0) # State Timer

            # whatIsThat = 5
            whatIsThat = 0
            calling_instance.writeVInt(whatIsThat)

            calling_instance.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

            calling_instance.writeString(playerData['Name']) # Player Name
            calling_instance.writeVInt(100)
            calling_instance.writeVInt(28000000 + playerData['Thumbnail']) # Player Thumbnail
            calling_instance.writeVInt(43000000 + playerData['Namecolor']) # Player Name Color
            calling_instance.writeVInt(46000000) # Color Gradients

            calling_instance.writeVInt(0)
            calling_instance.writeBoolean(False)

            thisThing = 0
            calling_instance.writeVInt(thisThing) # Club Leauge?
            calling_instance.writeVInt(0)

    @staticmethod
    def decode(calling_instance, fields):
        fields["AllianceFullEntry"] = {}
        fields["AllianceFullEntry"]["AllianceHeaderEntry"] = AllianceHeaderEntry.decode(calling_instance, fields)
        fields["AllianceFullEntry"]["Description"] = calling_instance.readString()
        fields["AllianceFullEntry"]["MemberCount"] = calling_instance.readVInt()
        return fields