from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.Wrappers.DeliveryUnit import DeliveryUnit
from Classes.Wrappers.GatchaDrop import GatchaDrop


class LogicGiveDeliveryItemsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        self.writeVInt(0)

        self.writeVInt(1) # array

        for i in range(1):
            DeliveryUnit.encode(self, [100, 1, [10, 0, 7, 0, 0, 0, i, i]])

        self.writeBoolean(False) # TODO: Forced Drops

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeDataReference(0, 0)

        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 201