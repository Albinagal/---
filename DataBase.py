import json


class JsonBase:
    def __init__(self, path: str):
        self.path = path

    def read(self) -> dict:
        with open(self.path, "r") as json_file:
            data = json.load(json_file)
            return data

    def add(self, new_data: dict):
        data = self.read()
        data.update(new_data)
        with open(self.path, 'w') as f:
            json.dump(data, f)
