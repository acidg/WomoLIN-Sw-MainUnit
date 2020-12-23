from util import to_hex, crc_modbus
from packets import packetFactory
import serial

TIMEOUT = 1.0

def capture(ser: serial.Serial):
    """ Reads the next data packet on the serial connection and returns it. Returns None, if read failed. """
    ser.timeout = TIMEOUT
    data = ser.read_until(b'\xaa')
    if data != b'\xaa':
        return None

    direction = ser.read()
    length = ser.read()
    address = ser.read(size=2)
    payload = ser.read(size=int(length[0]))
    crc = ser.read(size=2)
    if ser.read() != b'':
        print("data curruption during read")
        return None

    package_bytes = data + direction + length + address + payload

    if crc != crc_modbus(package_bytes):
        print("CRC missmatch")
        return None

    packet = packetFactory.create(address, payload)

    if packet is None:
        raise UnknownPacketError(package_bytes)


def get_addr_str(addr):
    return to_hex(addr) + "\t"


class UnknownPacketError(Exception):
    def __init__(self, data: bytearray):
        super().__init__()
        self.data = data

    def get_data(self):
        return self.data
