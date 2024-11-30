import Configuration
import os

from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData

StaticData.Preload()

if Configuration.settings["Testing"]:
    try:
        os.remove("Database/Files/player.sqlite")
        os.remove("Database/Files/club.sqlite")
    except:
        pass

ServerConnection(("0.0.0.0", Configuration.settings['Port']))