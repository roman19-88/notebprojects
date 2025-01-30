from typing import Any, Iterable


def filter_by_state(list_dictionary: Iterable[str], state_word: str = "EXECUTED") -> None:
    """Функция перебирает список словарей по ключу"""

    dict_state = []

    for elem in list_dictionary:
        if elem["state"] == state_word:
            dict_state.append(elem)

    return dict_state


def sort_by_date(data: Iterable[str]) -> None:
    """Функция сортирует по дате"""

    def data_get(item: Any) -> Any:
        """Функция вспомогающая, для сортировки"""
        return item["date"]

    return sorted(data, key=data_get, reverse=True)
