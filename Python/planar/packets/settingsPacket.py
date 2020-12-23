from packets.dataPacket import DataPacket
from util import to_hex

FUNCTION_ADDRESS = b'\x00\x02'

class SettingsPacket(DataPacket):
    """
    Settings packet containing settings of the heater
    """

    def __init__(self, payload: bytearray):
        super().__init__(payload)

    def __str__(self):
        return "Settings: (" + \
            "?: " + to_hex(self.payload[0:2]) + \
            ", By " + self.get_temp_source_str() + \
            ", Setpoint: " + str(int(self.payload[3])) + "°C" + \
            ", Ventilation: " + str(self.payload[4] == 0x01) + \
            ", Power: " + str(int(self.payload[5])) + "/9)"


    def get_temp_source_str(self):
        temp_source = self.payload[2]
        if temp_source == 0x01:
            return "Heater"
        elif temp_source == 0x02:
            return "Panel"
        elif temp_source == 0x03:
            return "Air"
        elif temp_source == 0x04:
            return "Power"
        return "UNKNOWN: " + to_hex(temp_source)
        

    @staticmethod
    def matches(address):
        return address == FUNCTION_ADDRESS

    def get_function_address(self):
        return FUNCTION_ADDRESS