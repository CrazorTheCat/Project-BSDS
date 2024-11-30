from Classes.ByteStream import ByteStream
from Classes.Debugger import Debugger

class StreamEntry:

    @staticmethod
    def encode(self: ByteStream, stream):
        Debugger.error(stream)
        self.encodeLogicLong(stream["StreamID"]) # StreamEntryID
        self.encodeLogicLong([0, 1]) # SenderID
        self.writeString(stream['PlayerName'])
        self.writeVInt(stream['PlayerRole'])
        self.writeVInt(0) # Time since Stream was sent
        self.writeBoolean(False)