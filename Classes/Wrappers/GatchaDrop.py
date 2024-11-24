
class GatchaDrop:

    @staticmethod
    def encode(calling_instance, fields):
        calling_instance.writeVInt(fields["GatchaAmount"])
        calling_instance.writeDataReference(*fields.get("GatchaCharacter", [0, 0]))
        calling_instance.writeVInt(fields["GatchaType"])
        calling_instance.writeDataReference(*fields.get("GatchaItem", [0, 0]))
        calling_instance.writeDataReference(*fields.get("GatchaEmote", [0, 0]))
        calling_instance.writeDataReference(*fields.get("GatchaSPG", [0, 0]))
        calling_instance.writeVInt(0) # Unknown, can't be implemented
        calling_instance.writeVInt(0) # Same goes for this

    @staticmethod
    def decode(calling_instance, fields):
        fields["GatchaDrop"] = {}
        fields["GatchaDrop"]["GatchaAmount"] = calling_instance.readVInt()
        fields["GatchaDrop"]["GatchaCharacter"] = calling_instance.readDataReference()
        fields["GatchaDrop"]["GatchaType"] = calling_instance.readVInt()
        fields["GatchaDrop"]["GatchaItem"] = calling_instance.readDataReference()
        fields["GatchaDrop"]["GatchaEmote"] = calling_instance.readDataReference()
        fields["GatchaDrop"]["GatchaSPG"] = calling_instance.readDataReference()
        fields["GatchaDrop"]["GatchaUnknown"] = calling_instance.readVInt()
        fields["GatchaDrop"]["GatchaUnknown2"] = calling_instance.readVInt()
        return fields