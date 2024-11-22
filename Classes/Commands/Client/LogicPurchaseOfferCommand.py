import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
from Static.StaticData import StaticData

OwnedPinsLatest = StaticData.Pins
OwnedThumbnailsLatest  = StaticData.Thumbnails
OwnedBrawlersLatest = StaticData.Brawlers


class LogicPurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk1"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        if fields["Unk1"] == 0:
            db_instance = DatabaseHandler()
            player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"] = OwnedBrawlersLatest[int(i)]["Skins"]
            player_data["OwnedPins"] = OwnedPinsLatest
            player_data["OwnedThumbnails"] = OwnedThumbnailsLatest
            db_instance.updatePlayerData(player_data, calling_instance)
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})

    def getCommandType(self):
        return 519