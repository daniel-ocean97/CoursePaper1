from functools import wraps
from pathlib import Path

from src.constants import json_report_path_file


def result_to_json_file(func):
    """Декоратор, который записывает результат выполнения функции в json файл в папке logs"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        json_string = func(*args, **kwargs)
        with open(json_report_path_file, "w", encoding="utf-8") as f:
            f.write(json_string)

    return wrapper


def result_to_json_named_file(file_name):
    """Декоратор, который записывает результат выполнения функции в указанный по имени json файл в папке logs"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_string = func(*args, **kwargs)
            path_file = Path(__file__).resolve().parent.parent / "logs" / file_name
            with open(path_file, "w", encoding="utf-8") as f:
                f.write(json_string)

        return wrapper

    return decorator
