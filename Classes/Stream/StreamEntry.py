from Classes.ByteStream import ByteStream
from Classes.Debugger import Debugger
from Classes.Logic.LogicLong import LogicLong

class StreamEntry:

    @staticmethod
    def encode(self: ByteStream, stream):
        self.encodeLogicLong(LogicLong(stream["StreamID"])) # StreamEntryID
        self.encodeLogicLong(LogicLong([0, 1])) # SenderID
        self.writeString(stream['PlayerName'])
        self.writeVInt(stream['PlayerRole'])
        self.writeVInt(0) # Time since Stream was sent
        self.writeBoolean(False)