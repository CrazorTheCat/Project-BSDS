import json
import random
import string

from Static.StaticData import StaticData


class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    AllianceID = [0, 0]
    Token = ""
    Name = "Brawler"
    Registered = False
    Thumbnail = 0
    Namecolor = 0
    Region = "CA"
    ContentCreator = "BSDS"

    Coins = 999999
    Gems = 999999
    StarPoints = 999999
    Trophies = 999999
    HighestTrophies = 999999
    TrophyRoadTier = 105
    Experience = 999999
    Level = 500
    Tokens = 200
    TokensDoubler = 1000

    SelectedSkins = {}
    SelectedBrawlers = [61, 60, 59]
    RandomizerSelectedSkins = []
    OwnedPins = StaticData.Pins 
    OwnedThumbnails = StaticData.Thumbnails
    OwnedBrawlers = StaticData.Brawlers

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 and lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'AllianceID': self.AllianceID,
            'Registered': self.Registered,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensDoubler': self.TokensDoubler,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
