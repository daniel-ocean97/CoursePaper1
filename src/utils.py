import json
import os
from datetime import datetime

import pandas as pd
import requests
from dotenv import load_dotenv
import logging
import os

# Создаем папку logs, если она не существует
os.makedirs('../logs', exist_ok=True)

# Настройка логгера
logging.basicConfig(
    filename='../logs/utils.log',  # Путь к файлу логов
    filemode='a',              # Режим открытия файла (добавление)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат логов
    level=logging.DEBUG         # Уровень логирования
)

load_dotenv()
currency_token = os.getenv("CURRENCY_API_KEY")
stocks_token = os.getenv("STOCKS_API_KEY")

with open("../user_settings.json", "r") as f:
    user_settings = json.load(f)


def greetings():
    current_time = datetime.now().hour  # Получаем текущий час
    if 5 <= current_time < 12:
        return "Доброе утро!"
    elif 12 <= current_time < 18:
        return "Добрый день!"
    elif 18 <= current_time < 22:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"



def cards_reading(end_date, start_date, df):
    logging.info('Начало работы функции cards_reading')
    filtered_df = df.loc[
        (df["Дата платежа"] >= start_date) & (df["Дата платежа"] <= end_date) & ((df["Сумма операции"]) < 0)
    ]
    logging.info('Отфильтрован Датафрейм по дате')
    result = filtered_df.groupby("Номер карты")["Сумма операции"].sum().round(2).reset_index()
    logging.info('Сгруппировал DataFrame по номеру карты и сумме операций')
    result["Кешбек"] = (result["Сумма операции"] / -100).round(2)
    logging.info('Успешное завершение работы функции cards_reading')
    return list(result.to_dict(orient="index").values())


def top_transactions(start_date, end_date, df):
    logging.info('Начало работы функции top_transactions')
    sorted_df = df.sort_values(by="Сумма операции", ascending=True)
    logging.info('DataFrame отсортирован по сумме операции')
    filtered_df = sorted_df.loc[(df["Дата платежа"] >= start_date) & (df["Дата платежа"] <= end_date)]
    result = filtered_df.head()
    result = result[["Дата операции", "Сумма операции с округлением", "Категория", "Описание"]]
    logging.info('Завершение работы функции top_transactions')
    return list(result.to_dict(orient="index").values())


def actual_currencies():
    final_result = []
    for currency in user_settings["user_currencies"]:
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount=1"

        payload = {}
        headers = {"apikey": currency_token}

        response = requests.request("GET", url, headers=headers, data=payload)

        api_result = response.json()
        temp_res = {"currency": currency, "rate": round(api_result["result"], 2)}
        final_result.append(temp_res)

    return final_result


def stock_prices():
    final_result = []
    for company in user_settings["user_stocks"]:
        symbol = company
        api_url = "https://api.api-ninjas.com/v1/stockprice?ticker={}".format(symbol)
        response = requests.get(api_url, headers={"X-Api-Key": stocks_token})
        if response.status_code == requests.codes.ok:
            api_result = response.json()
            temp_res = {"stock": symbol, "price": api_result["price"], "currency": api_result["currency"]}
            final_result.append(temp_res)
        else:
            print("Error:", response.status_code, response.text)

    return final_result
