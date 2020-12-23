from .settingsPacket import SettingsPacket
from .temperaturePacket import TemperaturePacket
from .statusPacket import StatusPacket
from util import to_hex


def create(address, payload):
    if SettingsPacket.matches(address):
        return SettingsPacket(payload)
    elif TemperaturePacket.matches(address):
        return TemperaturePacket(payload)
    elif StatusPacket.matches(address):
        return StatusPacket(payload)
    return None
