from src.views import greetings, cards_reading, top_transactions
from datetime import datetime
import pandas as pd

def main_page(date):
    """ Основная функция главной страница, принимает строку, а возвращает JSON файл"""
    result = {}
    end_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    start_date = end_date.replace(day=1)
    df = pd.read_excel("../data/operations.xlsx")
    df["Дата платежа"] = pd.to_datetime(df["Дата платежа"], dayfirst=True)
    result["greeting"] = greetings()
    result["cards"] = cards_reading(end_date, start_date, df)
    result["top_transactions"] = top_transactions(start_date, end_date, df)
    return result

print(main_page("2021-12-25 15:12:33"))