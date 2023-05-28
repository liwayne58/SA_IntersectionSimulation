import json


class Communication:
    def __init__(self, instruction=None, data=None):
        self.instruction = instruction
        self.data = data

    def toJson(self):
        return json.dumps(self.toDict())

    def toDict(self):
        return {
            "instruction": self.instruction,
            "data": self.data
        }


if __name__ == "__main__":
    obj = Communication()
    obj.instruction = "test"
    obj.data = "data"
    print(obj.toDict())
    print(obj.toJson())
