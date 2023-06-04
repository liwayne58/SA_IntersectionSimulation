from Enum.EnumDirection import EDirection
from Enum.EnumVehicle import EVehicle


class Vehicle:
    def __init__(self, EVehicle, lane, direction):
        self.vType = EVehicle.vType
        self.speed = EVehicle.speed
        self.direction = direction
        self.lane = lane


if __name__ == '__main__':
    obj = Vehicle(EVehicle.BIKE, 1, EDirection.EAST)
    print(obj.vType, obj.speed)
