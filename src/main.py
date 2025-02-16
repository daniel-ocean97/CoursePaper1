import json

from src.constants import DF
from src.decorators import result_to_json_file, result_to_json_named_file
from src.reports import expenses_by_category
from src.services import listed_df, search_transactions_by_mobile_phone
from src.views import main_page


def main():
    """Главная функция проекта, из неё можно получить доступ ко всем реализованным функциональностям"""
    print("Главная страница:")
    print(json.loads(main_page("2021-12-31 23:59:59", DF)))
    phone_search_query = input("Произвести ли поиск транзакций, где в описании указан номер телефона? да/нет\n")
    if phone_search_query.lower() == "да":
        print(search_transactions_by_mobile_phone(listed_df))
    transactions_report_query = input("Произвести отчёт по транзакциями за последние 3 месяца категории? да/нет\n")
    if transactions_report_query.lower() == "да":
        category_query = input("Укажите категорию:\n")
        report_to_file = input("Хотите ли записать результат отчёта в файл? да/нет\n")
        if report_to_file.lower() == "да":
            report_to_named_file = input("Хотите ли сами указать имя файла?\n")
            if report_to_named_file.lower() == "да":
                name_of_file = input(
                    "Укажите имя файл латиницей (что бы файл был в json формате необходимо в конце добавить '.json': \n"
                )
                decorated_function = result_to_json_named_file(name_of_file)(expenses_by_category)
                decorated_function(DF, category_query, "31.12.2021 23:59:59")

            else:
                decorated_function = result_to_json_file(expenses_by_category)
                decorated_function(DF, category_query, "31.12.2021 23:59:59")

        else:
            print(expenses_by_category(DF, category_query, "31.12.2021 23:59:59"))

    print("Конец работы приложения")
