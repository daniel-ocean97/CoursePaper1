import json
from datetime import datetime
import os
from pathlib import Path

import pandas as pd

from src.utils import actual_currencies, cards_reading, greetings, stock_prices, top_transactions

data_file_path = Path(__file__).resolve().parent.parent / "data" / "operations.xlsx"


df = pd.read_excel(data_file_path)
df["Дата платежа"] = pd.to_datetime(df["Дата платежа"], dayfirst=True)



def main_page(date, data):
    """Основная функция главной страница, принимает строку, а возвращает JSON файл"""
    result = {}
    end_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    start_date = end_date.replace(day=1)
    result["greeting"] = greetings()
    result["cards"] = cards_reading(end_date, start_date, data)
    result["top_transactions"] = top_transactions(start_date, end_date, data)
    result["currency_rates"] = actual_currencies()
    result["stock_prices"] = stock_prices()
    json_result = json.dumps(result, ensure_ascii=False, indent=4)
    return json_result


print(main_page("2021-12-25 15:12:33", df))
