from enum import Enum


class EInstruction(Enum):
    REQUIRE_DATA_TRAFFIC_PERIOD = 0,
    REQUIRE_DATA_CURRENT_TRAFFIC_STATE = 1,

    SEND_DATA_TRAFFIC_PERIOD = 2,
    SEND_DATA_CURRENT_TRAFFIC_STATE = 3,

    SWITCH_MODE = 4


if __name__ == "__main__":
    print(EInstruction.EAST.value)
