from POJO.TrafficSinal import TrafficSignal
from Enum.EnumDirection import EDirection
from Enum.EnumVehicle import EVehicle
from Enum.EnumLane import ELane


class Road:
    def __init__(self, direction, isPrimary=None):
        self.defaultPeriod = None
        self.isPrimary = isPrimary
        self.crossed = 0
        self.existVehicle = {
            EVehicle.MOTORCYCLE.name: 0,
            # EVehicle.BUS.name: 0,
            EVehicle.HEAVYVEHICLE.name: 0,
            EVehicle.CAR.name: 0
        }
        self.lane = {
            ELane.First.value: [],
            ELane.Second.value: [],
            ELane.Third.value: [],
        }
        self.direction = direction
        self.trafficSignals = TrafficSignal()


if __name__ == '__main__':
    obj = Road(EDirection.EAST)
