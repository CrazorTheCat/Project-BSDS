from Classes.Wrappers.GatchaDrop import GatchaDrop

class DeliveryUnit:

    @staticmethod
    def encode(calling_instance, field, fields):
        calling_instance.writeVInt(field)
        calling_instance.writeVInt(len(fields["DeliveryItems"]))
        for i in fields["DeliveryItems"]:
            GatchaDrop.encode(calling_instance, i)

    @staticmethod
    def decode(calling_instance, fields):
        fields["DeliveryUnit"] = {}
        fields["DeliveryUnit"]["DeliveryType"] = calling_instance.readVInt()
        fields["DeliveryUnit"]["GatchaItemCount"] = calling_instance.readVInt()
        for i in range(fields["DeliveryUnit"]["GatchaItemCount"]):
            GatchaDrop.decode(calling_instance, fields)

        return fields