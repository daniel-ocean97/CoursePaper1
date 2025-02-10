import logging
import os
from datetime import datetime

import requests

from src.constants import currency_token, stocks_token, user_settings

# Создаем папку logs, если она не существует
os.makedirs("../logs", exist_ok=True)

# Настройка логгера
logging.basicConfig(
    filename="../logs/utils.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат логов
    level=logging.DEBUG,  # Уровень логирования
)


def greetings():
    """Функция, возвращающая приветствие в зависимости от времени суток"""
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
    """Функция, предоставляющая информацию расходов по картам"""
    logging.info("Starting cards_reading")
    filtered_df = df.loc[
        (df["Дата платежа"] >= start_date) & (df["Дата платежа"] <= end_date) & ((df["Сумма операции"]) < 0)
    ]
    logging.info("Filter DF by fate")
    result = filtered_df.groupby("Номер карты")["Сумма операции"].sum().round(2).reset_index()
    logging.info("Group DataFrame")
    result["Кешбек"] = (result["Сумма операции"] / -100).round(2)
    logging.info("Successful completion of the function")
    return list(result.to_dict(orient="index").values())


def top_transactions(start_date, end_date, df):
    """Функция, показывающая топ-5 трат за указанный период"""
    logging.info("Starting top_transactions")
    sorted_df = df.sort_values(by="Сумма операции", ascending=True)
    logging.info("DataFrame sotred")
    filtered_df = sorted_df.loc[(df["Дата платежа"] >= start_date) & (df["Дата платежа"] <= end_date)]
    result = filtered_df.head()
    result = result[["Дата операции", "Сумма операции с округлением", "Категория", "Описание"]]
    logging.info("Successful completion of the function")
    return list(result.to_dict(orient="index").values())


def actual_currencies():
    """Функция, которая показывает актуальные курсы валют"""
    logging.info("Starting actual_currencies")
    final_result = []
    for currency in user_settings["user_currencies"]:
        logging.info("Connect to API")
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency}&amount=1"

        payload = {}
        headers = {"apikey": currency_token}

        response = requests.request("GET", url, headers=headers, data=payload)

        api_result = response.json()
        temp_res = {"currency": currency, "rate": round(api_result["result"], 2)}
        final_result.append(temp_res)
    logging.info("Successful completion of the function")
    return final_result


def stock_prices():
    """Функция, которая показывает актуальные цены на акции"""
    logging.info("Starting stock_prices")
    final_result = []
    for company in user_settings["user_stocks"]:
        logging.info("Connect to API")
        symbol = company
        api_url = "https://api.api-ninjas.com/v1/stockprice?ticker={}".format(symbol)
        response = requests.request("GET", api_url, headers={"X-Api-Key": stocks_token})
        api_result = response.json()
        temp_res = {"stock": symbol, "price": api_result["price"], "currency": api_result["currency"]}
        final_result.append(temp_res)

    logging.info("Successful completion of the function")

    return final_result
