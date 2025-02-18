import json

from src.reports import expenses_by_category


def test_expenses_by_category(data_for_reports_test):
    """Функция для тестирования expenses_by_category"""
    expected_result = json.dumps(
        {
            "Категория": "Еда",
            "Сумма операции с округлением": 380
        },
        ensure_ascii=False,
        indent=4,
    )

    assert expenses_by_category(data_for_reports_test, category="Еда") == expected_result
