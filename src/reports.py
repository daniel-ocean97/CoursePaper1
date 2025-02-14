from datetime import datetime
import pandas as pd
from src.constants import DF
from dateutil.relativedelta import relativedelta
import json
from src.decorators import result_to_file


@result_to_file
def expenses_by_category(data, category, date=datetime.now()):
    if type(date) == str:
        end_date = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    else:
        end_date = date
    start_date = end_date - relativedelta(months=3)
    data["Дата платежа"] = pd.to_datetime(data["Дата платежа"], dayfirst=True)
    filtered_df = data.loc[
        (data["Дата платежа"] >= start_date) & (data["Дата платежа"] <= end_date) & ((data["Сумма операции"]) < 0)
        ]
    temp_result = filtered_df.groupby('Категория')[['Сумма операции', 'Описание']].agg(list).reset_index()
    temp_result = list(temp_result.to_dict(orient="index").values())
    result = []
    for expense in temp_result:
        if expense["Категория"] == category:
            for i in range(len(expense["Сумма операции"])):
                result.append({"Сумма операции": expense["Сумма операции"][i], "Описание": expense["Описание"][i]})
    return json.dumps(result, ensure_ascii=False, indent=4)



expenses_by_category(DF, "Супермаркеты", "31.12.2021 16:44:00")