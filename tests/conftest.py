import pytest
import pandas as pd
from src.views import df


@pytest.fixture
def transactions_data():
    # Чтение данных из Excel файла
    df_test = df

    # Преобразование данных в список словарей для удобства использования в тестах

    return df_test

