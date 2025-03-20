import re

from black.trans import defaultdict

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers_files_csv_excel import csv_read, excel_read
from src.utils import operations_finances
from src.widget import get_date, mask_account_card


def filter_transaction_by_word(transaction, filter_word):
    """поиск по ключевому слову"""
    patern = re.compile(re.escape(filter_word), re.IGNORECASE)
    return [t for t in transaction if patern.search(t.get("description", ""))]


def count_transactions_by_category(transactions, categories):
    """возвращает категории операций"""
    categories_count = defaultdict(int)
    for transaction in transactions:
        category = transaction.get("description")
        if category in categories:
            categories_count[category] += 1
    return dict(categories_count)


def main():
    """главная функция с логикой"""
    while True:

        print(
            """\nПривет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
        )

        try:
            file_extension = int(input())
        except ValueError:
            continue

        if file_extension == 1:
            print("\nДля обработки выбран JSON-файл\n")
            dict = operations_finances("operations.json")

            break
        elif file_extension == 2:
            print("\nДля обработки выбран CSV-файл\n")
            dict = csv_read("C://Users//admin//PycharmProjects//notebproject//data//transactions.csv")
            break
        elif file_extension == 3:
            print("\nДля обработки выбран XLSX-файл\n")
            dict = excel_read("C://Users//admin//PycharmProjects//notebproject//data//transactions_excel.xlsx")
            break
        else:
            print("\nТакого пункта не существует\n")

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )

        filter_status = input().upper()

        if filter_status == "EXECUTED":
            filtered_state_dict = filter_by_state(list_dictionary=dict, state_word=filter_status)
            print('\nОперации отфильтрованы по статусу "EXECUTED"\n')
            break

        elif filter_status == "CANCELED":
            filtered_state_dict = filter_by_state(list_dictionary=dict, state_word=filter_status)
            print('\nОперации отфильтрованы по статусу "CANCELED"\n')
            break

        elif filter_status == "PENDING":
            filtered_state_dict = filter_by_state(list_dictionary=dict, state_word=filter_status)
            print('\nОперации отфильтрованы по статусу "PENDING"\n')
            break
        else:
            print(f'\nСтатус операции "{filter_status}" недоступен.\n')

    print("Отсортировать операции по дате? Да/Нет\n")
    sorted_by_date = input()

    if sorted_by_date.lower() == "да":
        while True:
            print("\nОтсортировать по возрастанию или по убыванию?\n")
            sort_order = input()

            if sort_order.lower() == "по возрастанию":
                sorted_by_date = sort_by_date(data=filtered_state_dict, reverse_order=False)
                break
            elif sort_order.lower() == "по убыванию":
                sorted_by_date = sort_by_date(data=filtered_state_dict, reverse_order=True)
                break
            else:
                print("\nТакой сортировки не существует\n")
    elif sorted_by_date.lower() == "нет":
        sorted_by_date = filtered_state_dict

    while True:
        print("\nВыводить только рублевые транзакции? Да/Нет\n")
        ruble_transactions = input()

        if ruble_transactions.lower() == "да":

            rub_transactions = filter_by_currency(transactions=sorted_by_date, currency="RUB")
            currency_transactions = []

            for transaction in rub_transactions:
                currency_transactions.append(transaction)

            break
        elif ruble_transactions.lower() == "нет":
            currency_transactions = sorted_by_date
            break
        else:
            print("\nТакого ответа не существует\n")

    while True:
        print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        filtered_transactions = input()
        if filtered_transactions.lower() == "да":
            print("\nВведите слово:\n")
            filter_word = input()
            filter_by_word_dict = filter_transaction_by_word(currency_transactions, filter_word)
            break

        elif filtered_transactions.lower() == "нет":
            filter_by_word_dict = currency_transactions
            break
        else:
            print("\nТакого ответа не существует\n")

    print("\nРаспечатываю итоговый список транзакций...")

    print(f"\nВсего банковских операций в выборке: {len(filter_by_word_dict)}\n")
    if not filter_by_word_dict:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    for transaction in filter_by_word_dict:
        print(
            f"""
{get_date(transaction['date'])} {transaction['description']}
{mask_account_card(transaction['to'])}
{int(float(transaction['operationAmount']['amount'])) if file_extension == 1 else int(float(transaction['amount']))} {transaction['operationAmount']['currency']['name'] if file_extension == 1 else transaction['currency_name']}"""
        )


if __name__ == "__main__":
    main()
