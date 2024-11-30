import time
import threading
import traceback

import Configuration
from Classes.Debugger import Debugger
from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Player import Player
from Classes.MessageManager import MessageManager
from Classes.Messaging import Messaging


class Connection(threading.Thread):
    def __init__(self, socket, address):
        super().__init__()
        self.client = socket
        self.address = address
        self.player = Player()
        self.lastSentPacketTime = time.time()

    def recv(self, n):
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                return b''
            data.extend(packet)
        return data

    def run(self):
        try:
            while True:
                messageHeader = self.client.recv(7)
                if len(messageHeader) >= 7:
                    headerData = Messaging.readHeader(messageHeader)
                    self.lastSentPacketTime = time.time()
                    packetPayload = Connection.recv(self, headerData[1])
                    MessageManager.receiveMessage(self, headerData[0], packetPayload)

                timeNow = time.time()
                if (timeNow - self.lastSentPacketTime) > 7:
                    Debugger.warning(f"Client {self.address} disconnected.")
                    ClientsManager.RemovePlayer(self.client, self.player.ID)
                    self.client.close()
                    break


        except Exception:
            Debugger.error(f"Exception with client {self.address}, Closing connection...")
            ClientsManager.RemovePlayer(self.client, self.player.ID)
            self.client.close()
            if Configuration.settings["Verbose"]:
                Debugger.error(traceback.format_exc())