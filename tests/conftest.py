from datetime import datetime, timedelta

import pandas as pd
import pytest

from src.constants import DF


@pytest.fixture
def transactions_data():
    """Функция для определения фикстуры transactions_data"""
    df_test = DF
    df_test["Дата платежа"] = pd.to_datetime(DF["Дата платежа"], dayfirst=True)
    return df_test


@pytest.fixture()
def search_mobile_data():
    """Функция для определения фикстуры search_mobile_data"""
    return [
        {
            "Дата операции": "18.11.2021 21:15:27",
            "Дата платежа": "19.11.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -200.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -200.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Мобильная связь",
            "MCC": None,
            "Описание": "Тинькофф Мобайл +7 995 555-55-55",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 200.0,
        },
        {
            "Дата операции": "18.12.2021 21:15:27",
            "Дата платежа": "19.12.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -200.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -200.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Продукты",
            "MCC": None,
            "Описание": "Пятерочка",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 200.0,
        },
    ]


@pytest.fixture
def data_for_reports_test():
    data = {
        "Категория": ["Еда", "Транспорт", "Еда", "Развлечения", "Транспорт", "Еда", "Развлечения"],
        "Сумма операции с округлением": [100, 50, 200, 150, 30, 80, 120],
        "Сумма операции": [-100, -50, -200, -150, -30, -80, -120],
        "Описание": ["Обед", "Такси", "Продукты", "Кино", "Автобус", "Кофе", "Концерт"],
        "Дата платежа": [
            (datetime.now() - timedelta(days=10)).strftime("%d.%m.%Y %H:%M:%S"),
            (datetime.now() - timedelta(days=40)).strftime("%d.%m.%Y %H:%M:%S"),
            (datetime.now() - timedelta(days=70)).strftime("%d.%m.%Y %H:%M:%S"),
            (datetime.now() - timedelta(days=20)).strftime("%d.%m.%Y %H:%M:%S"),
            (datetime.now() - timedelta(days=50)).strftime("%d.%m.%Y %H:%M:%S"),
            (datetime.now() - timedelta(days=5)).strftime("%d.%m.%Y %H:%M:%S"),
            (datetime.now() - timedelta(days=90)).strftime("%d.%m.%Y %H:%M:%S"),
        ],
        "Дополнительная информация": [
            "Оплата картой",
            "Наличные",
            "Оплата картой",
            "Оплата картой",
            "Наличные",
            "Оплата картой",
            "Оплата картой",
        ],
    }
    return pd.DataFrame(data)
