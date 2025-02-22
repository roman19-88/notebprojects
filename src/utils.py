import json
import logging
import os

dir_name_log = os.path.dirname(__file__)
file_path_log = os.path.join(dir_name_log, '..', 'logs', 'utils.log')
logger = logging.getLogger('utils')
file_handler = logging.FileHandler(file_path_log, encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def operations_finances(file_name):
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logger.info('Принял путь до нужного JSON файла')

    dir_name = os.path.dirname(__file__)
    file_path = os.path.join(dir_name, '..', 'data', file_name)

    try:
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)
            logger.info('Открыл файл')
            if len(data) == 0:
                logger.warning('Нет данных в файле')
                return []

            logger.info('Вернул список словарей с данными о финансах')
            return data

    except json.JSONDecodeError as error:
        logger.error(f"Ошибка при чтении файла: {error}", exc_info=True)
        return []
