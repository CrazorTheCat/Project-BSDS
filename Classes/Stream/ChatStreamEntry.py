from Classes.ByteStream import ByteStream
from Classes.Stream.StreamEntry import StreamEntry

class ChatStreamEntry:
    def encode(self: ByteStream, info):
        StreamEntry.encode(self, info)
        self.writeString(info['Message'])
        self.writeBoolean(False) # what is this? it seems new