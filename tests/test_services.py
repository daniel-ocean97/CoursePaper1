from src.services import search_transactions_by_mobile_phone


def test_search_transactions_by_mobile_phone(search_mobile_data):
    """ Функция для тестирования search_transactions_by_mobile_phone """
    expected_result = """[
    {
        "Дата операции": "18.11.2021 21:15:27",
        "Дата платежа": "19.11.2021",
        "Номер карты": null,
        "Статус": "OK",
        "Сумма операции": -200.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -200.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": null,
        "Категория": "Мобильная связь",
        "MCC": null,
        "Описание": "Тинькофф Мобайл +7 995 555-55-55",
        "Бонусы (включая кэшбэк)": 2,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 200.0
    }
]"""
    assert search_transactions_by_mobile_phone(search_mobile_data) == expected_result
