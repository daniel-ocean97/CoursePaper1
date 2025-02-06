from datetime import datetime
import pandas as pd

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

date = "2021-12-25 15:12:33"

end_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
start_date = end_date.replace(day=1)
df = pd.read_excel("../data/operations.xlsx")
df["Дата платежа"] = pd.to_datetime(df["Дата платежа"], dayfirst=True)


def cards_reading(end_date, start_date, df):
    filtered_df = df.loc[(df["Дата платежа"] >= start_date) &
                     (df["Дата платежа"] <= end_date) & ((df["Сумма операции"]) < 0)]

    result = filtered_df.groupby("Номер карты")["Сумма операции"].sum().round(2).reset_index()
    result["Кешбек"] = (result["Сумма операции"] / -100).round(2)

    return list(result.to_dict(orient='index').values())


def top_transactions(start_date, end_date, df):
    sorted_df = df.sort_values(by='Сумма операции', ascending=True)
    filtered_df = sorted_df.loc[(df["Дата платежа"] >= start_date) &
                     (df["Дата платежа"] <= end_date)]
    result = filtered_df.head()
    result = result[["Дата операции", "Сумма операции с округлением", "Категория", "Описание"]]
    return list(result.to_dict(orient='index').values())


#top_transactions(start_date, end_date, df)