from enum import Enum


class EDirection(Enum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3


if __name__ == "__main__":
    print(EDirection.EAST.value)
