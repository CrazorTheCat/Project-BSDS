from Classes.Packets.PiranhaMessage import PiranhaMessage

class LoginFailedMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeInt(fields['ErrorID'])

        self.writeString(fields.get("FingerprintData", None)) # Fingerprint
        self.writeString() # Redirect URL
        self.writeString(fields.get('ContentURL', None))
        self.writeString(fields.get("UpdateURL", None)) # "Update Available!" URL
        self.writeString(fields.get('Message', None))

        self.writeInt(fields.get("MaintenanceTime", 0)) # Maintenance Time Left
        self.writeBoolean(False) # Show Support Page

        self.writeBytes(b'', 0) # Compressed Fingerprint

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString()
        self.writeInt(0)
        self.writeBoolean(True)
        self.writeBoolean(True)
        self.writeString()
        self.writeVInt(0)
        self.writeString()
        self.writeBoolean(False)

    def decode(self):
        fields = {}
        fields["ErrorCode"] = self.readInt()
        fields["ResourceFingerprintData"] = self.readString()
        fields["RedirectDomain"] = self.readString()
        fields["ContentURL"] = self.readString()
        fields["UpdateURL"] = self.readString()
        fields["Reason"] = self.readString()
        fields["SecondsUntilMaintenanceEnd"] = self.readInt()
        fields["ShowContactSupportForBan"] = self.readBoolean()
        fields["CompressedFingerprintData"] = self.readBytesWithoutLength()
        fields["ContentURLListCount"] = self.readInt()
        fields["ContentURLList"] = []
        for i in range(fields["ContentURLListCount"]):
            fields["ContentURLList"].append(self.readString())
        fields["KunlunAppStore"] = self.readInt()
        fields["MaintenanceType"] = self.readInt()
        fields["HelpshiftFaqId"] = self.readString()
        fields["Tier"] = self.readInt()
        fields["Unk1"] = self.readBoolean()
        fields["Unk2"] = self.readBoolean()
        fields["Unk3"] = self.readString()
        fields["Unk4"] = self.readVInt()
        fields["Unk5"] = self.readString()
        fields["OptionalTargetedAccountIdState"] = self.readBoolean()
        if fields["OptionalTargetedAccountIdState"]:
            fields["OptionalTargetedAccountId"] = self.readLong()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20103

    def getMessageVersion(self):
        return self.messageVersion