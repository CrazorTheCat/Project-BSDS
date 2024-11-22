from PlayerThumbnails import PlayerThumbnails
from Pins import Pins
from Skins import Skins
from Characters import Characters
from Cards import Cards

brawlerIds = Characters.getBrawlersID()
final = {}

def GetBrawlersList():
    for brawlerId in brawlerIds:
        cardId = Cards.getBrawlerUnlockID(brawlerId)
        skinsIds = Skins.getBrawlerSkins(brawlerId)
        final[brawlerId] = {'CardID': cardId, 'Skins': skinsIds, 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2}

    for i in final:
        print(str(i) + ":", str(final[i]) + ",")

def GetPins():
    print(Pins.getPinsID())

def GetPlayerThumbnails():
    print(PlayerThumbnails.getThumbnailsID())

#GetBrawlersList()
#GetPins()
#GetPlayerThumbnails()