from POJO.TrafficSinal import TrafficSignal
from Enum.EnumDirection import EDirection
from Enum.EnumLane import ELane


class Road:
    def __init__(self, direction, isPrimary=None):
        self.defaultPeriod = None
        self.isPrimary = isPrimary
        self.crossed = 0
        self.lane = {
            ELane.First.value: [],
            ELane.Second.value: [],
            ELane.Third.value: [],
        }
        self.direction = direction
        self.trafficSignals = TrafficSignal()


if __name__ == '__main__':
    obj = Road(EDirection.EAST)
