from typing import Union
from typing import Any
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(numbers: Any) -> Any:
    """Создаем новую функцию, которая также макскирует номер, но теперь с названием счета (карты)"""
    new_numbers = numbers.split(' ')
    if 'Счет' in numbers:
        return f'Счет {get_mask_account(numbers)}'
    else:
        return f'{' '.join(new_numbers[0:-1])} {get_mask_card_number(new_numbers[-1])}'


def get_date(date: Union[str]) -> Union[str, int]:
    """Создаем функцию, которая возвращает дату в'ДД.ММ.ГГГГ'"""

    return f'ДД.ММ.ГГГГ ( {date[5:7]}.{date[8:10]}.{date[0:4]} )'
