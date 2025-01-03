from Classes.Packets.PiranhaMessage import PiranhaMessage

class AllianceLeagueMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeBoolean(True)  # Alliance League Week Active?
        # AllianceLeague::encode
        if self.writeBoolean(True):  # sub_A380A8
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(99999)
            self.writeVInt(4)

            self.writeVInt(3)  # Events || sub_3CE7F4
            events = [7, 25, 8]
            for x in range(3):
                self.writeVInt(x + 1)  # IndexSlot
                self.writeVInt(4)  # Unknown
                self.writeDataReference(15, events[x])  # Location ID
                self.writeVInt(0)  # Unknown
                self.writeBoolean(True)

        if self.writeBoolean(True):  # LeagueStateEntry::encode
            self.writeVLong(*player.AllianceID)  # AllianceID
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVLong(*player.AllianceID)  # Unknown
            self.writeVInt(1)  # Current Day
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(True)  # ?
            self.writeVInt(9999)  # Score
            self.writeVInt(1)  # Leaderboard Place
            self.writeVInt(0)

        if self.writeBoolean(True):  # PlayerLeagueData::encode
            self.writeVLong(*player.AllianceID)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(3)
            self.writeVInt(0)

        if self.writeBoolean(True):
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(99999)
            self.writeVInt(4)

            self.writeVInt(3)  # Events
            events = [7, 25, 8]
            for x in range(3):
                self.writeVInt(x + 1)  # IndexSlot
                self.writeVInt(4)  # Unknown
                self.writeDataReference(15, events[x])  # Location ID
                self.writeVInt(0)  # Unknown
                self.writeBoolean(True)


    def decode(self):
        fields = {}
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 22161

    def getMessageVersion(self):
        return self.messageVersion