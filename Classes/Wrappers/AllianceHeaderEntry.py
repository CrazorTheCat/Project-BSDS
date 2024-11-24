from Classes.Files.Classes.Regions import Regions

class AllianceHeaderEntry:
    @staticmethod
    def encode(calling_instance, clubdb, clubData):
        calling_instance.writeLong(clubData["HighID"], clubData["LowID"])
        calling_instance.writeString(clubData["Name"])
        calling_instance.writeDataReference(8, clubData["BadgeID"])
        calling_instance.writeVInt(clubData["Type"])
        calling_instance.writeVInt(len(clubData["Members"]))
        calling_instance.writeVInt(clubdb.getTotalTrophies(clubData))
        calling_instance.writeVInt(clubData["TrophiesRequired"])
        calling_instance.writeDataReference(0)
        calling_instance.writeString(Regions.getRegionByID(calling_instance, clubData["RegionID"]))
        calling_instance.writeVInt(0)
        calling_instance.writeBoolean(clubData["FamilyFriendly"])
        calling_instance.writeVInt(0)

    @staticmethod
    def decode(calling_instance, fields):
        fields["AllianceHeaderEntry"] = {}
        fields["AllianceHeaderEntry"]["AllianceID"] = calling_instance.readLong()
        fields["AllianceHeaderEntry"]["AllianceName"] = calling_instance.readString()
        fields["AllianceHeaderEntry"]["AllianceBadge"] = calling_instance.readDataReference()
        fields["AllianceHeaderEntry"]["AllianceType"] = calling_instance.readVInt()
        fields["AllianceHeaderEntry"]["AllianceMembersCount"] = calling_instance.readVInt()
        fields["AllianceHeaderEntry"]["AllianceTrophies"] = calling_instance.readVInt()
        fields["AllianceHeaderEntry"]["AllianceTrophiesRequired"] = calling_instance.readVInt()
        fields["AllianceHeaderEntry"]["AllianceUnknown"] = calling_instance.readDataReference() # Could just be VInt, but incase its different
        fields["AllianceHeaderEntry"]["AllianceRegion"] = calling_instance.readString()
        fields["AllianceHeaderEntry"]["AllianceUnknown2"] = calling_instance.readVInt()
        fields["AllianceHeaderEntry"]["AllianceFriendly"] = calling_instance.readBoolean()
        fields["AllianceHeaderEntry"]["AllianceUnknown3"] = calling_instance.readVInt()
        return fields