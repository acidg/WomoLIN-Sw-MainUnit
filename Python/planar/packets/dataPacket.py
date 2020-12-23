import libscrc

class DataPacket(object):
    """
    Packet of data sent between the heater and the remote
    """

    def __init__(self, payload: bytearray):
        self.payload = payload

    def length(self):
        return len(self.payload)

    def get_payload(self):
        return self.payload

    @staticmethod
    def matches(self, address):
        return False

    def get_function_address(self):
        raise AssertionError("Implementation missing. Please implement get_function_address")

    def get_sendable_bytes(self):
        data_bytes = b'\xaa\x03'
        data_bytes += bytes([self.length()])
        data_bytes += self.get_function_address()
        data_bytes += self.get_payload()
        
        return data_bytes + libscrc.modbus(data_bytes)
