import json
import logging
import os
import re

from src.constants import DF

listed_df = list(DF.to_dict(orient="index").values())

# Создаем папку logs, если она не существует
os.makedirs("../logs", exist_ok=True)

# Настройка логгера
logging.basicConfig(
    filename="../logs/services.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат логов
    level=logging.DEBUG,  # Уровень логирования
)


def search_transactions_by_mobile_phone(data):
    """Функция для поиска мобильных номеров в описании транзакций"""
    logging.info("Started function search_transactions_by_mobile_phone")
    result = []
    logging.info("Determining the pattern of phone number search")
    mobile_pattern = re.compile(r"\+\d{1,4}")
    logging.info("Phone number search")
    for transaction in data:
        if mobile_pattern.search(transaction["Описание"]):
            result.append(transaction)
    logging.info("Successful completion of the function")
    return json.dumps(result, ensure_ascii=False, indent=4)
