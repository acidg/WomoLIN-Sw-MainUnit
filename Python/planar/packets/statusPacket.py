from packets.dataPacket import DataPacket
from util import to_hex


class StatusPacket(DataPacket):
    """
    Status packet containing the status of the heater
    """

    def __init__(self, payload: bytearray):
        super().__init__(payload)

    def __str__(self):
        if len(self.payload) == 0:
            return "Status Request"
        return "Status Response: [" + to_hex(self.payload) + "] (" + \
            "?: " + to_hex(self.payload[0]) + \
            ",?: " + to_hex(self.payload[1]) + \
            ", Error code: " + to_hex(self.payload[2]) + \
            ", Temp: " + str(int(self.payload[3])) + "°C" + \
            ", ?: " + to_hex(self.payload[4:6]) + \
            ", Voltage: " + str(int(self.payload[6])/10) + "V" + \
            ", ?: " + to_hex(self.payload[7:]) + ")"

    @staticmethod
    def matches(address):
        return address == b'\x00\x0F'
