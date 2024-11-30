import json
import os
import time
import random

import Configuration


class Utility:
    def parseFields(fields: dict):
        print()
        for typeName,value in fields.items():
            print(f"{typeName}: {value}")
        print()

    def getContentUpdaterInfo():
        return open(f"./ContentUpdater/lastversion.txt", 'r').read().split('...')

    def getFingerprintData(resourceSha):
        return json.dumps(json.loads(open(f"./ContentUpdater/Update/{resourceSha}/fingerprint.json", 'r').read()))

    def getRandomID():
        id = []
        id.append(int(''.join([str(random.randint(0, 9)) for _ in range(2)])))
        id.append(int(''.join([str(random.randint(0, 9)) for _ in range(8)])))
        return id
