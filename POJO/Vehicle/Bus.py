from Enum.EnumDirection import EDirection
from Enum.EnumVehicle import EVehicleType


class Bus:
    def __init__(self, direction):
        self.speed = 1.8
        self.direction = direction
        self.vType = EVehicleType.BIKE


if __name__ == '__main__':
    obj = Bus(EDirection.EAST)
