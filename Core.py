import socket
import threading
import traceback
from builtins import ConnectionError

from Logic.Client.ClientsManager import ClientsManager
from Logic.Data.PacketsHandler import PacketsHandler
from Logic.Client.PlayerManager import Players

'''brawlertrophies = 1500
ProgressStart = [501, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
ProgressEnd = [524, 549, 574, 599, 624, 649, 674, 699, 724, 749, 774, 799, 824, 849, 874, 899, 924, 949, 974, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, -1]
Progress = [500, 524, 549, 574, 599, 624, 649, 674, 699, 724, 749, 774, 799, 824, 849, 874, 885, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1150]
RewardedSP = [20, 50, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350]

if brawlertrophies >= 1500:
    print(brawlertrophies, RewardedSP[Progress.index(1150)], brawlertrophies - 1150)
if brawlertrophies >= 501:
    for i in Progress:
        if ProgressStart[Progress.index(i)] <= brawlertrophies <= ProgressEnd[Progress.index(i)]:
            print(brawlertrophies, RewardedSP[Progress.index(i)], brawlertrophies - i)
            break
else:
    print("Trophies below 501.")'''

class Core:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def CoreInit(self):
        self.server.bind(('0.0.0.0', 9339))
        print("Socket binded!")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            print(f'Got new connection with address: {address[0]}')
            ConnectionThread(socket, address).start()

class ConnectionThread(threading.Thread):
    def __init__(self, client, address):
        super().__init__()
        self.address = address
        self.client = client
        self.player = Players

    def run(self):
        try:
            while True:
                # Reading and processing packet
                PacketsHandler.ReadHeader(self)

        except ConnectionError:
            print(f"Client with ip: {self.address[0]} disconnected!")
            ClientsManager.RemoveSocket(self.player.LowID)
            self.client.close()
            print(traceback.format_exc())
            exit(0)

Core().CoreInit()