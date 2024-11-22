
class GatchaDrop:
    def encode(calling_instance, fields):
        calling_instance.writeVInt(fields[0])
        calling_instance.writeDataReference(0, 0)
        calling_instance.writeVInt(fields[2])
        calling_instance.writeDataReference(0, 0)
        calling_instance.writeDataReference(0, 0)
        calling_instance.writeDataReference(0, 0)
        calling_instance.writeVInt(fields[6])
        calling_instance.writeVInt(fields[7])

    def decode(calling_instance, fields):
        fields["GatchaDrop"] = {} # TODO: this thing
        return fields