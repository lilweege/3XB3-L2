from os import path
import csv


def check_file_exists(filename: str) -> None:
    if not path.exists(filename):
        raise ValueError(f'Unkown file [{filename}]')


def read_csv_contents(filename):
    '''
    Open a csv file named <filename> and read the contents into a list of dicts
    '''

    def autoconvert(value):
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        if value == "NULL":
            return None
        return value

    with open(filename, "r", encoding='utf-8-sig') as file:
        return [{k: autoconvert(v) for k, v in row.items()}
                for row in csv.DictReader(file, delimiter=',', quotechar='"')]
