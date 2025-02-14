import json


def result_to_file(func):
    def wrapper(*args, **kwargs):
        with open("report.json", "w", encoding="utf-8") as f:
            json.dump(func(*args, **kwargs), f, ensure_ascii=False, indent=4)
    return wrapper