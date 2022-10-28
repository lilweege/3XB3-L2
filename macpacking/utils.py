from os import path

def check_file_exists(filename: str) -> None:
    if not path.exists(filename):
        raise ValueError(f'Unkown file [{filename}]')