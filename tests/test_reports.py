import json

from src.reports import expenses_by_category


def test_expenses_by_category(data_for_reports_test):
    """Функция для тестирования expenses_by_category"""
    expected_result = json.dumps(
        [
            {"Сумма операции": -100, "Описание": "Обед"},
            {"Сумма операции": -200, "Описание": "Продукты"},
            {"Сумма операции": -80, "Описание": "Кофе"},
        ],
        ensure_ascii=False,
        indent=4,
    )

    assert expenses_by_category(data_for_reports_test, category="Еда") == expected_result
