from enum import Enum


class EVehicleType(Enum):
    CAR = ("CAR", 2.25)
    BUS = ("BUS", 1.8)
    TRUCK = ("TRUCK", 1.8)
    BIKE = ("BIKE", 2.5)

    def __new__(cls, vType: str, speed: float):
        obj = object.__new__(cls)
        obj._vType_ = vType
        obj.speed = speed
        return obj

    def __init__(self, vType: str, speed: float) -> None:
        self.vType = vType
        self.speed = speed


if __name__ == "__main__":
    print(EVehicleType.BIKE.vType)
