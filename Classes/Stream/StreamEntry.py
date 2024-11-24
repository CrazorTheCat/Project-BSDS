from Classes.ByteStream import ByteStream

class StreamEntry:

    @staticmethod
    def encode(self: ByteStream, stream):
        self.writeLogicLong(*stream["StreamID"]) # StreamEntryID
        self.writeLogicLong(*[0, 1]) # SenderID
        self.writeString(stream['PlayerName'])
        self.writeVInt(stream['PlayerRole'])
        self.writeVInt(0) # Time since Stream was sent
        self.writeBoolean(False)