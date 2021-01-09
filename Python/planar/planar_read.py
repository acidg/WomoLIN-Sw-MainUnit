import serial
import sys
import binascii
from util import to_hex, crc_modbus, from_hex
from packets import packetFactory
from planar_interface import capture_serial, UnknownPacketError


def main():
    serial_heater = serial.Serial('/dev/ttyUSB1', 2400, timeout=1.0)

    while True:
        try:
            command = read_command()
            if command is None:
                continue
            command = b'\xaa\x03' + command # aa = packet start, 03 = targeting heater
            command = command + crc_modbus(command)
            print("Sending:\t["+ to_hex(command) + "]")
            serial_heater.write(command)
        except ValueError as e:
            print("Invalid input: " + str(e))
            continue

        try:
            packet = capture_serial(serial_heater)
            print("Received:\t" + str(packet))
        except UnknownPacketError as e:
            print("Received unknown packet (crc ok): ", to_hex(e.get_data()))


def read_command():
    print("Input: ", end="")
    line = str(sys.stdin.readline())
    line = line.rstrip("\n")
    line = line.strip()
    return from_hex(line)


if __name__ == "__main__":
    main()
