import json
import os


def load_json():
    """Чтение json-файла"""
    with open(os.path.join('operations.json'), 'r', encoding = "utf-8") as read_file:
        data = json.load(read_file)
        return data
