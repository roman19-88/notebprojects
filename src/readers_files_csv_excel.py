import pandas as pd


def csv_read(path_name):
    """функция чтения csv файла"""
    df = pd.read_csv(path_name, delimiter=';')
    df_dict = df.to_dict(orient='records')
    return df_dict


def excel_read(path_name):
    """функция чтения excel файла"""
    df = pd.read_excel(path_name)
    df_dict_excel = df.to_dict(orient='records')
    return df_dict_excel
