import traceback

from Classes.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
from Classes.Debugger import Debugger

class MessageManager:
    def receiveMessage(self, messageType, messagePayload):
        message = LogicLaserMessageFactory.createMessageByType(messageType, messagePayload)
        if message is not None:
            try:
                if message.isServerToClient():
                    message.encode()
                else:
                    message.execute(self, message.decode())

            except Exception:
                Debugger.error(traceback.format_exc())