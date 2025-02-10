from unittest.mock import Mock, patch

import pytest

from src.utils import actual_currencies, cards_reading, greetings, stock_prices, top_transactions


# Параметризация теста: кортежи из (время, ожидаемое приветствие)
@pytest.mark.parametrize(
    "time, expected",
    [
        (5, "Доброе утро!"),
        (11, "Доброе утро!"),
        (12, "Добрый день!"),
        (17, "Добрый день!"),
        (18, "Добрый вечер!"),
        (21, "Добрый вечер!"),
        (22, "Доброй ночи!"),
        (4, "Доброй ночи!"),
    ],
)
def test_greetings(time, expected):
    """ Функция для тестирования greetings """
    # Используем patch для мокирования метода now() класса datetime
    with patch("src.utils.datetime") as mock_datetime:
        # Устанавливаем возвращаемое значение для метода now().hour
        mock_datetime.now.return_value.hour = time

        # Вызываем тестируемую функцию и проверяем результат
        assert greetings() == expected


def test_cards_reading(transactions_data):
    """ Функция для тестирования cards_reading """
    assert cards_reading("2021-12-25 15:12:33", "2021-12-01 15:12:33", transactions_data) == [
        {"Номер карты": "*4556", "Сумма операции": -952.9, "Кешбек": 9.53},
        {"Номер карты": "*5091", "Сумма операции": -13136.0, "Кешбек": 131.36},
        {"Номер карты": "*7197", "Сумма операции": -18525.69, "Кешбек": 185.26},
    ]


def test_top_transactions(transactions_data):
    """ Функция для тестирования top_transactions """
    assert top_transactions("2021-12-01 15:12:33", "2021-12-25 15:12:33", transactions_data) == [
        {
            "Дата операции": "22.12.2021 23:30:44",
            "Сумма операции с округлением": 28001.94,
            "Категория": "Переводы",
            "Описание": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
        {
            "Дата операции": "16.12.2021 16:40:47",
            "Сумма операции с округлением": 14216.42,
            "Категория": "ЖКХ",
            "Описание": "ЖКУ Квартира",
        },
        {
            "Дата операции": "23.12.2021 16:14:59",
            "Сумма операции с округлением": 10000.0,
            "Категория": "Переводы",
            "Описание": "Светлана Т.",
        },
        {
            "Дата операции": "02.12.2021 16:26:02",
            "Сумма операции с округлением": 5510.8,
            "Категория": "Каршеринг",
            "Описание": "Ситидрайв",
        },
        {
            "Дата операции": "14.12.2021 11:04:32",
            "Сумма операции с округлением": 5000.0,
            "Категория": "Переводы",
            "Описание": "Светлана Т.",
        },
    ]


@patch("requests.request")
def test_actual_currencies(mock_request):
    """ Функция для тестирования actual_currencies """
    mock_response = Mock()
    mock_response.json.return_value = {"result": 100.123}
    mock_request.return_value = mock_response
    assert actual_currencies() == [{"currency": "USD", "rate": 100.12}, {"currency": "EUR", "rate": 100.12}]


@patch("requests.request")
def test_stock_prices(mock_request):
    """ Функция для тестирования stock_prices """
    mock_response = Mock()
    mock_response.json.return_value = {"price": 322.8, "currency": "USD"}
    mock_request.return_value = mock_response
    assert stock_prices() == [
        {"stock": "AAPL", "price": 322.8, "currency": "USD"},
        {"stock": "AMZN", "price": 322.8, "currency": "USD"},
        {"stock": "GOOGL", "price": 322.8, "currency": "USD"},
        {"stock": "MSFT", "price": 322.8, "currency": "USD"},
        {"stock": "TSLA", "price": 322.8, "currency": "USD"},
    ]
