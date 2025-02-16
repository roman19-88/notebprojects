import json
import os


def operations_finances(file_name):
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    dir_name = os.path.dirname(__file__)
    file_path = os.path.join(dir_name, '..', 'data', file_name)
    try:
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)

            if len(data) == 0:
                return []
            return data
    except (json.JSONDecodeError) as error:
        print(f"Ошибка при чтении файла: {error}")
        return []
