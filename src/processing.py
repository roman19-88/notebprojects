from typing import Any


def filter_by_state(list_dictionary: Any) -> Any:
    """ Функция сортирующая список словарей по 'EXECUTED'"""
    dict_state = []
    for i in list_dictionary:
        if i['state'] == 'EXECUTED':
            dict_state.append(i)
    return dict_state


def sort_by_date(data: Any) -> Any:
    """Функция сортирующая дату"""

    def data_get(item):
        return item['date']

    return sorted(data, key=data_get, reverse=True)
