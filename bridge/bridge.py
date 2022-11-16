from abc import ABC


class Device(ABC):

    def is_enabled(self) -> bool:
        pass

    def disable(self):
        pass

    def enable(self):
        pass


class Remote:

    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            pass
        else:
            self.device.enable()


class Tv(Device):
    _enabled = False

    def is_enabled(self):
        return self._enabled

    def disable(self):
        self._enabled = False

    def enable(self):
        self._enabled = True


class AdvancedRemote(Remote):

    def force_power(self):
        self.device.disable()
