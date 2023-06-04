from enum import Enum
import random


class EVehicle(Enum):
    CAR = ("CAR", 2.25)
    # BUS = ("BUS", 1.8)
    HEAVYVEHICLE = ("TRUCK", 1.8)
    MOTORCYCLE = ("BIKE", 2.5)

    def __new__(cls, vType: str, speed: float):
        obj = object.__new__(cls)
        obj._vType_ = vType
        obj.speed = random.uniform(1.2, 2.5)
        return obj

    def __init__(self, vType: str, speed: float) -> None:
        self.vType = vType
        self.speed = random.uniform(1.2, 2.5)


if __name__ == "__main__":
    print(EVehicle.BIKE.vType)
