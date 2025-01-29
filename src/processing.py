
from typing import Any, Iterable, Union


def filter_by_state(list_dictionary: Iterable[str], state_word: Iterable[str]) -> Iterable[str]:
  """ Функция сортирующая список словарей по ключу """
    dict_state = []

    for elem in list_dictionary:
        if elem["state"] == state_word:
            dict_state.append(elem)

    return dict_state


def sort_by_date(data: Union[int, str]) -> Union[int, str]:
  """Функция сортирующая дату"""
    def data_get(item: Any) -> Any:
        return item["date"]
