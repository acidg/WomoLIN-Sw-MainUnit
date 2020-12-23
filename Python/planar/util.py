import binascii
import libscrc


def to_hex(data: bytearray):
    if data is None:
        return ""
    if type(data) == int:
        return binascii.hexlify(bytes([data])).decode()
    return binascii.hexlify(data, " ").decode()


def from_hex(hex_data: str):
    return bytes.fromhex(hex_data)


def crc_modbus(data: bytearray):
    check = libscrc.modbus(data)
    return check.to_bytes(2, "big")
