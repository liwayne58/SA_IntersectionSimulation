from Enum.EnumDirection import EDirection
from Enum.EnumVehicle import EVehicleType


class Bike:
    def __init__(self, lane, direction):
        self.speed = 2.5
        self.direction = direction
        self.lane = lane
        self.vType = EVehicleType.BIKE


if __name__ == '__main__':
    obj = Bike(1, EDirection.EAST)
