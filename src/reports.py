import json
import logging
import os
from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta

# Создаем папку logs, если она не существует
os.makedirs("../logs", exist_ok=True)

# Настройка логгера
logging.basicConfig(
    filename="../logs/reports.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат логов
    level=logging.DEBUG,  # Уровень логирования
)


def expenses_by_category(data, category, date=datetime.now()):
    """Функция, которая выводит все транзакции по указанной категории за три месяца от указанной даты"""
    logging.info("Started function expenses_by_category")
    if type(date) == str:
        logging.info("Processing date user input")
        end_date = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    else:
        end_date = date
    start_date = end_date - relativedelta(months=3)
    data["Дата платежа"] = pd.to_datetime(data["Дата платежа"], dayfirst=True)
    filtered_df = data.loc[
        (data["Дата платежа"] >= start_date) & (data["Дата платежа"] <= end_date) & ((data["Сумма операции"]) < 0)
    ]
    logging.info("Filtering by date")
    temp_result = filtered_df.groupby("Категория")["Сумма операции с округлением"].sum().reset_index()
    temp_result = list(temp_result.to_dict(orient="index").values())
    for current in temp_result:
        if current["Категория"] == category.title():
            result = current
            return json.dumps(result, ensure_ascii=False, indent=4)
    return "Указанной категории не существует"


