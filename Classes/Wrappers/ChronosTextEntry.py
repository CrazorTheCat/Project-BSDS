from Classes.ByteStream import ByteStream

class ChronosTextEntry:
    @staticmethod
    def decode(byteStream: ByteStream):
        fields = []
        fields.append(byteStream.readInt())
        fields.append(byteStream.readStringReference())
        return fields

    @staticmethod
    def encode(byteStream: ByteStream, stringType: int, string: str):
        byteStream.writeInt(stringType)
        byteStream.writeStringReference(string)