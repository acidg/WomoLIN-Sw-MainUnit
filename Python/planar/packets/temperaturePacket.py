from packets.dataPacket import DataPacket


class TemperaturePacket(DataPacket):
    """
    Command packet sent from the remote to the heater containing the temperature of the remote
    """

    def __init__(self, payload: bytearray):
        super().__init__(payload)

    @staticmethod
    def matches(address: bytearray):
        return address == b'\x00\x11'

    def get_temperature(self):
        temp = self.payload[0]
        return str(int(temp)) + "°C"

    def __str__(self):
        return "Temperature: " + self.get_temperature()
