from signal import signal, SIGINT
import sys
from util import to_hex, crc_modbus, from_hex
from planar_interface import capture_stdin, UnknownPacketError

# Pipe output of following command to this script:
# sigrok-cli -d fx2lafw:conn=1.42 -c samplerate=20k -C D0,D1 --continuous -P uart:baudrate=2400 -B uart


def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    sys.exit(0)


def main():
    signal(SIGINT, handler)

    while True:
        try:
            packet = capture_stdin()
            if str(type(packet)) == "<class 'packets.statusPacket.StatusPacket'>":
                print(str(packet))
        except UnknownPacketError as e:
            print("unknown packet (crc ok): ", to_hex(e.get_data()))


if __name__ == "__main__":
    main()
