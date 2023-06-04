from Enum.EnumDirection import EDirection
from Enum.EnumVehicle import EVehicle


class Car:
    def __init__(self, direction):
        self.speed = 2.25
        self.direction = direction
        self.vType = EVehicle.BIKE


if __name__ == '__main__':
    obj = Car(EDirection.EAST)
