from packets.dataPacket import DataPacket
from util import to_hex


class StatusPacket(DataPacket):
    """
    Status packet containing the status of the heater
    """

    def __init__(self, payload: bytearray):
        super().__init__(payload)

    def __str__(self):
        return "Status: (" + \
            "?: " + to_hex(self.payload[0]) + \
            ((", Error code: " + self.get_error()) if self.payload[1] == 0x01 else "") + \
            ", Temp: " + str(int(self.payload[3])) + "°C" + \
            ", ?: " + to_hex(self.payload[4:6]) + \
            ", Voltage: " + str(int(self.payload[6])/10) + "V" + \
            ", ?: " + to_hex(self.payload[7:]) + ")"

    def get_error(self):
        return str(int(self.payload[2]))

    @staticmethod
    def matches(address):
        return address == b'\x00\x0F'
