import Configuration
from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData

StaticData.Preload()

ServerConnection(("0.0.0.0", Configuration.settings['Port']))