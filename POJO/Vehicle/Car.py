from Enum.EnumDirection import EDirection
from Enum.EnumVehicle import EVehicleType


class Car:
    def __init__(self, direction):
        self.speed = 2.25
        self.direction = direction
        self.vType = EVehicleType.BIKE


if __name__ == '__main__':
    obj = Car(EDirection.EAST)
