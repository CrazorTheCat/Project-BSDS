import Configuration
import traceback

from Classes.Debugger import Debugger

class ClientsManager:

    PlayersList = {}

    def AddPlayer(playerID, socket, connection):
        if ClientsManager.PlayersList.keys().__contains__(playerID[1]):
            ClientsManager.RemovePlayer(playerID)
        ClientsManager.PlayersList[playerID[1]] = {"Socket": socket, "Connection": connection}

    def RemovePlayer(client, playerID):
        try:
            allSockets = ClientsManager.GetAll()
            if playerID[1] in allSockets.keys() and allSockets[playerID[1]]["Socket"] == client:
                ClientsManager.PlayersList.pop(playerID[1])
        except KeyError:
            Debugger.error(f"Cannot remove socket with id: {playerID} Reason: {playerID} is not in the list.")
        except Exception:
            if Configuration.settings["Vebose"]:
                Debugger.info(f"Error not handled correctly traceback:\n{traceback.format_exc()}")

    def GetAll():
        return ClientsManager.PlayersList

    def GetCount():
        return len(ClientsManager.PlayersList)