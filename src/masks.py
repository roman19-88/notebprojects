from typing import Union



def get_mask_card_number(number: Union[int]) -> Union[str]:
    """ Создаем функцию, которая принимает номер карты и возвращает маску номера карты"""
    str_number = str(number)
    return f'{str_number[0:4]} {str_number[4:6]}** **** {str_number[12:16]}'


def get_mask_account(number_score: Union[int]) -> Union[str]:
    """Создаем функцию, которая принимает номер счет и возвращает маску номера счета"""
    str_number_score = str(number_score)
    return f'**{str_number_score[-4:]}'
