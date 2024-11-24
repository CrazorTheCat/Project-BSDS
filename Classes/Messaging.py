import traceback
from Classes.ClientsManager import ClientsManager

class Messaging:
    @staticmethod
    def writeHeader(message, payloadLen):
        message.messageBuffer += message.getMessageType().to_bytes(2, 'big', signed=True)
        message.messageBuffer += payloadLen.to_bytes(3, 'big', signed=True)
        message.messageBuffer += message.messageVersion.to_bytes(2, 'big', signed=True)

    @staticmethod
    def readHeader(headerBytes): # :2 for MessageID and 2:5 for MessageLength
        return [int.from_bytes(headerBytes[:2], 'big', signed=True),
                      int.from_bytes(headerBytes[2:5], 'big', signed=True)]

    @staticmethod
    def sendMessage(messageType, fields, player=None, playerIDs=None, item = None):
        from Classes.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
        message = LogicLaserMessageFactory.createMessageByType(messageType, b'')
        if not playerIDs:
            if player is not None:
                message.encode(fields, player)
            else:
                message.encode(fields)
            Messaging.writeHeader(message, len(message.messagePayload))
            message.messageBuffer += message.messagePayload
            try:
                fields["Socket"].send(message.messageBuffer)
            except Exception:
                print(traceback.format_exc())
        else:
            for pl in playerIDs:
                message.clear(0)
                if item is None: data = ClientsManager.PlayersList.get(pl[1], None)
                else: data = ClientsManager.PlayersList.get(pl[item], None)
                if data is None: continue
                try:
                    message.encode(fields)
                except TypeError:
                    message.encode(fields, data["Connection"].player)
                Messaging.writeHeader(message, len(message.messagePayload))
                message.messageBuffer += message.messagePayload
                try:
                    data["Socket"].send(message.messageBuffer)
                except BrokenPipeError:
                    continue