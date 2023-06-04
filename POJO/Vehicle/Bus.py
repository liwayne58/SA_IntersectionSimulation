from Enum.EnumDirection import EDirection
from Enum.EnumVehicle import EVehicle


class Bus:
    def __init__(self, direction):
        self.speed = 1.8
        self.direction = direction
        self.vType = EVehicle.BIKE


if __name__ == '__main__':
    obj = Bus(EDirection.EAST)
