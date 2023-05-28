from enum import Enum


class ESignal(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2


if __name__ == "__main__":
    print(ESignal.RED)
