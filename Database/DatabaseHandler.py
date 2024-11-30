import json
import sqlite3
import traceback

from Classes.Debugger import Debugger
from Classes.Files.Classes.Regions import Regions

class DatabaseHandler():
    def __init__(self):
        self.conn = sqlite3.connect("Database/Files/player.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (ID int, Token text, Data json)""")
        except sqlite3.OperationalError:
            pass
        except Exception:
            print(traceback.format_exc())

    def createAccount(self, data):
        try:
            self.cursor.execute("INSERT INTO main (ID, Token, Data) VALUES (?, ?, ?)", (data["ID"][1], data["Token"], json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception:
            print(traceback.format_exc())

    def getAll(self):
        self.playersId = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                self.playersId.append(self.db[i][0])
            return self.playersId
        except Exception:
            print(traceback.format_exc())

    def getPlayer(self, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            return json.loads(self.cursor.fetchall()[0][2])
        except Exception:
            print(traceback.format_exc())

    def getPlayerEntry(self, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            return self.cursor.fetchall()[0]
        except IndexError:
            pass
        except Exception:
            print(traceback.format_exc())

    def loadAccount(self, player, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            playerData = json.loads(self.cursor.fetchall()[0][2])
            player.ID = playerData["ID"]
            player.Name = playerData["Name"]
            player.AllianceID = playerData["AllianceID"]
            player.Registered = playerData["Registered"]
            player.Thumbnail = playerData["Thumbnail"]
            player.Namecolor = playerData["Namecolor"]
            player.Region = playerData["Region"]
            player.ContentCreator = playerData["ContentCreator"]
            player.Coins = playerData["Coins"]
            player.Gems = playerData["Gems"]
            player.StarPoints = playerData["StarPoints"]
            player.Trophies = playerData["Trophies"]
            player.HighestTrophies = playerData["HighestTrophies"]
            player.TrophyRoadTier = playerData["TrophyRoadTier"]
            player.Experience = playerData["Experience"]
            player.Level = playerData["Level"]
            player.Tokens = playerData["Tokens"]
            player.TokensDoubler = playerData["TokensDoubler"]
            player.SelectedBrawlers = playerData["SelectedBrawlers"]
            player.OwnedPins = playerData["OwnedPins"]
            player.OwnedThumbnails = playerData["OwnedThumbnails"]
            player.OwnedBrawlers = playerData["OwnedBrawlers"]
        except Exception:
            print(traceback.format_exc())

    def updatePlayerData(self, data, calling_instance):
        try:
            self.cursor.execute("UPDATE main SET Data=? WHERE ID=?", (json.dumps(data, ensure_ascii=False), calling_instance.player.ID[1]))
            self.conn.commit()
            self.loadAccount(calling_instance.player, calling_instance.player.ID)
        except Exception:
            print(traceback.format_exc())

    def playerExist(self, loginToken, loginID):
        try:
            if loginID[1] in self.getAll():
                if loginToken != self.getPlayerEntry(loginID)[1]:
                    return False
                return True
            return False
        except Exception:
            print(traceback.format_exc())

class ClubDatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect("Database/Files/club.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (LowID integer, Data json)""")
        except:
            pass

    def createClub(self, lowID, data):
        try:
            self.cursor.execute("INSERT INTO main (LowID, Data) VALUES (?, ?)",
                                (lowID, json.dumps(data, ensure_ascii=False)))
            self.conn.commit()
        except Exception as e:
            print(e)

    def deleteClub(self, lowID):
        try:
            self.cursor.execute("DELETE FROM main where LowID=?", (lowID,))
            self.conn.commit()
        except Exception as e:
            print(e)


    def getAllClub(self):
        clubs = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                clubs.append(json.loads(self.db[i][1]))
            return clubs
        except Exception as e:
            print(e)

    def getAllClubByRegion(self, regionID):
        clubs = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                dataLoaded = json.loads(self.db[i][1])
                if dataLoaded['RegionID'] == Regions.getIDByRegion(self, regionID):
                    clubs.append(dataLoaded)
            return clubs
        except Exception as e:
            print(traceback.format_exc())

    def getDefaultMembersData(self, player, role):
        return {'HighID': player.ID[0], 'LowID': player.ID[1], 'Name': player.Name, 'Role': role, 'Trophies': player.Trophies, 'NameColor': player.Namecolor, 'Thumbnail': player.Thumbnail}

    def getDefaultMessageData(self, eventType, streamType, lastID, playerID, playerName, playerRole, target={}, msgData="", premadeID=-1, messageDataID=-1):
        return {'StreamType': eventType, 'EventType': streamType, 'StreamID': lastID, 'PlayerID': playerID, 'PlayerName': playerName, 'PlayerRole': playerRole, 'Message': msgData, 'Target': target, 'PremadeID': premadeID, 'MessageDataID': messageDataID}

    def getClubWithLowID(self, low):
        try:
            self.cursor.execute("SELECT * from main where LowID=?", (low,))
            return self.cursor.fetchall()
        except Exception as e:
            Debugger.error(f"[ClubDatabaseHandler::getClubWithLowID] Unable to get Alliance/Club with LowID {low}, error: {e}")
            return "{}" # Making json.loads not throw an error

    def getMembersSorted(self, clubdata):
        try:
            return sorted(clubdata['Members'], key = lambda x: x['Trophies'], reverse=True)
        except Exception as e:
            print(e)

    def getMemberWithLowID(self, clubData, playerLowID) -> dict:
        '''
        Gets a Club Member from the playerLowID specified. playerLowID parameter must be an Integer
        :param clubData:
        :param playerLowID:
        :return:
        '''
        try:
            for m in clubData["Members"]:
                if m["LowID"] == playerLowID: return m
        except Exception as e:
            print(e)

    def getMemberWithID(self, clubData, playerID: list) -> dict:
        '''
        Gets a Club Member from the playerID specified. playerID parameter must be a List
        :param clubData:
        :param playerID:
        :return:
        '''
        try:
            for m in clubData["Members"]:
                if [m["HighID"], m["LowID"]] == playerID: return m
        except Exception as e:
            print(e)

    def getTotalTrophies(self, clubData):
        try:
            totalTrophies = 0
            for i in clubData["Members"]:
                totalTrophies += i['Trophies']
            return totalTrophies
        except Exception as e:
            print(e)

    def LoadAccount(self, low, player):
        try:
            self.player = player
            self.cursor.execute("SELECT * from main where LowID=?", (low,))
            self.players = self.cursor.fetchall()
            self.players = json.loads(self.players[0][2])
        except Exception as e:
            print(e)

    def updateClubData(self, data, lowID):
        try:
            self.cursor.execute("UPDATE main SET Data=? WHERE LowID=?", (json.dumps(data, ensure_ascii=False), lowID))
            self.conn.commit()
        except Exception as e:
            print(traceback.format_exc())