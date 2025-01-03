import zlib
from io import BufferedReader, BytesIO

from Classes.Logic.LogicLong import LogicLong
from Classes.Debugger import Debugger


class ByteStreamHelper:

    def readDataReference(self) -> list:
        high: int = self.readVInt()
        if high > 0:
            low: int = self.readVInt()
        else:
            low: int = 0

        return [high, low]

    def writeDataReference(self, high=0, low=-1):
        self.writeVInt(high)
        if high > 0:
            self.writeVInt(low)

    def compress(self, data):
        compressedText = zlib.compress(data)
        self.writeInt(len(compressedText) + 4)
        self.writeIntLittleEndian(len(data))
        self.buffer += compressedText

    def decompress(self):
        data_length = self.readInt()
        self.readIntLittleEndian()
        return zlib.decompress(self.readBytes(data_length - 4))

    def decodeIntList(self):
        length = self.readVInt()
        intList = []
        for i in range(length):
            intList.append(self.readVInt())
        return intList

    def decodeLogicLong(self, logicLong=None) -> list:
        if logicLong is None:
            logicLong = LogicLong(0, 0)
        high = self.readVInt()
        logicLong.high = high
        low = self.readVInt()
        logicLong.low = low
        return [high, low]

    def decodeLogicLongList(self) -> list[LogicLong]:
        length = self.readVInt()
        logicLongList = []
        for i in range(length):
            logicLongList.append(LogicLong(self.readVInt(), self.readVInt()))
        return logicLongList

    def encodeIntList(self, intList):
        length = len(intList)
        self.writeVInt(length)
        for i in intList:
            self.writeVInt(i)

    def encodeLogicLong(self, logicLong):
        if logicLong is None:
            logicLong = LogicLong(0, 0)
        self.writeVInt(logicLong.getHigherInt())
        self.writeVInt(logicLong.getLowerInt())

    def encodeLogicLongList(self, logicLongList):
        length = len(logicLongList)
        self.writeVInt(length)
        for logicLong in logicLongList:
            self.writeVInt(logicLong.getHigherInt())
            self.writeVInt(logicLong.getLowerInt())