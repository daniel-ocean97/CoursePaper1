import json
import re

from src.constants import DF

listed_df = list(DF.to_dict(orient="index").values())


def search_transactions_by_mobile_phone(data):
    """ Функция для поиска мобильных номеров в описании транзакций """
    result = []
    mobile_pattern = re.compile(r"\+\d{1,4}")
    for transaction in data:
        if mobile_pattern.search(transaction["Описание"]):
            result.append(transaction)
    return json.dumps(result, ensure_ascii=False, indent=4)
