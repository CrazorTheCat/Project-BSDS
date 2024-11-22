from Classes.Files.Classes.Regions import Regions
from Classes.Wrappers.GatchaDrop import GatchaDrop


class DeliveryUnit:
    def encode(calling_instance, fields):
        calling_instance.writeVInt(fields[0])
        calling_instance.writeVInt(fields[1])
        for i in range(fields[1]):
            GatchaDrop.encode(calling_instance, fields[2])

    def decode(calling_instance, fields):
        fields["DeliveryUnit"] = {} # TODO: this thing
        return fields