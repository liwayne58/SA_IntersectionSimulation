from Enum.EnumSignal import ESignal


class TrafficSignal:
    def __init__(self):
        self.currentSignal = None
        self.previousSignal = None
        self.signalStates = {
            ESignal.GREEN.name: 0,
            ESignal.YELLOW.name: 0,
            ESignal.RED.name: 0,
        }

    def setSignal(self, signal):
        self.previousSignal = signal
        self.currentSignal = signal

    def switchNextSignal(self):
        if self.currentSignal == ESignal.GREEN:
            self.currentSignal = ESignal.YELLOW
        elif self.currentSignal == ESignal.YELLOW and self.previousSignal == ESignal.GREEN:
            self.currentSignal = ESignal.RED
            self.previousSignal = ESignal.RED
        elif self.currentSignal == ESignal.YELLOW and self.previousSignal == ESignal.RED:
            self.currentSignal = ESignal.GREEN
            self.previousSignal = ESignal.GREEN
        elif self.currentSignal == ESignal.RED:
            self.currentSignal = ESignal.YELLOW


if __name__ == '__main__':
    obj = TrafficSignal()
