from Classes.ByteStream import ByteStream
from Classes.Stream.StreamEntry import StreamEntry


class ChatStreamEntry:
    def encode(self: ByteStream, info):
        print('angry')
        StreamEntry.encode(self, info)
        self.writeString(info['Message'])