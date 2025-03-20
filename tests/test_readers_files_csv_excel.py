import unittest
from unittest.mock import patch

import pandas as pd

from src.readers_files_csv_excel import csv_read, excel_read

"""тесты для функций считывания CSV и EXCEL файла"""


@patch('pandas.read_csv')  # Мокаем pandas.read_csv
def test_csv_read(mock_read_csv):
    mock_data = [
        {'Date': '2025-03-01', 'Description': 'Transfer', 'Amount': 1000},
        {'Date': '2025-03-02', 'Description': 'Payment', 'Amount': -500},
        {'Date': '2025-03-03', 'Description': 'Deposit', 'Amount': 200}
    ]

    mock_read_csv.return_value = pd.DataFrame(mock_data)

    result = csv_read('path/to/your/csvfile.csv')

    assert result == mock_data, f"Expected {mock_data}, but got {result}"

    mock_read_csv.assert_called_with('path/to/your/csvfile.csv', delimiter=';')


if __name__ == '__main__':
    unittest.main()


@patch('pandas.read_excel')
def test_excel_read(mock_read_excel):
    mock_data = [
        {'Date': '2025-03-01', 'Description': 'Transfer', 'Amount': 1000},
        {'Date': '2025-03-02', 'Description': 'Payment', 'Amount': -500},
        {'Date': '2025-03-03', 'Description': 'Deposit', 'Amount': 200}
    ]

    mock_read_excel.return_value = pd.DataFrame(mock_data)

    result = excel_read('path/to/your/excelfile.xlsx')

    assert result == mock_data, f"Expected {mock_data}, but got {result}"

    mock_read_excel.assert_called_with('path/to/your/excelfile.xlsx')


if __name__ == '__main__':
    unittest.main()
