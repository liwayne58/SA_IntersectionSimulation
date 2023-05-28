from enum import Enum


class ELane(Enum):
    First = 0
    Second = 1
    Third = 2


if __name__ == "__main__":
    print(ELane.First.value)
