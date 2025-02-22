import os
import pytest
from src.decorators import log

"""тесты для декоратора"""


@log()
def add(a, b):
    return a + b


# Тестирование логирования в консоль
def test_log_to_console(capsys):
    # Вызов функции, которая будет логировать в консоль
    add(1, 2)

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()

    # Проверяем, что консольный вывод правильный
    assert captured.out.strip() == "add ok"


# Тестирование логирования в файл
def test_log_to_file():
    log_filename = 'test_log.txt'

    # Убедимся, что файл не существует перед тестом
    if os.path.exists(log_filename):
        os.remove(log_filename)

    @log(log_filename)
    def add(a, b):
        return a + b

    # Вызов функции, которая будет логировать в файл
    add(3, 4)

    # Проверяем, что файл существует и записано правильное сообщение
    assert os.path.exists(log_filename)

    with open(log_filename, 'r') as file:
        content = file.read().strip()

    assert content == "add ok"

    # Удаляем файл после теста
    os.remove(log_filename)


# Тестирование ошибок
def test_log_with_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    try:
        divide(1, 0)  # Деление на ноль вызовет ошибку
    except Exception:
        # Перехватываем вывод в консоль
        captured = capsys.readouterr()
        # Проверяем, что ошибка была правильно записана в консоль
        assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out.strip()


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
