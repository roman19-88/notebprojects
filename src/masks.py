import logging
import os
from typing import Union

dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, '..', 'logs', 'masks.log')
logger = logging.getLogger('masks')
file_handler = logging.FileHandler(file_path, encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number: Union[int]) -> Union[str]:
    """Создаем функцию, которая принимает номер карты и возвращает маску номера карты"""
    logger.info('Номер карты принят в работу')

    str_number = str(number)
    if len(str_number) == 16 and len(str_number) >= 0:
        logger.info('Номер карты замаскирован успешно')

        return f"{str_number[0:4]} {str_number[4:6]}** **** {str_number[12:16]}"
    else:
        logger.warning('Не хватает цифр, пожалуйста введите 16 цифр')


def get_mask_account(number_score: Union[int]) -> Union[str]:
    """Создаем функцию, которая принимает номер счет и возвращает маску номера счета"""

    str_number_score = str(number_score)
    logger.info('Номер счета принят в работу')
    if len(str_number_score) == 20 and len(str_number_score) >= 0:
        logger.info('Номер счета замаскирован успешно')
        return f"**{str_number_score[-4:]}"
    else:
        logger.info('Не хватает цифр, пожалуйста введите 16 цифр')


if __name__ == '__main__':
    get_mask_card_number('7000792289606361')
    get_mask_account('73654108430135874305')
