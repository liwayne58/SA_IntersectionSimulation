from enum import Enum


class EMode(Enum):
    NORMAL = 0
    TRAFFIC_JAM = 1
    EMERGENCY = 2


if __name__ == "__main__":
    print(EMode.EAST.NORMAL)
