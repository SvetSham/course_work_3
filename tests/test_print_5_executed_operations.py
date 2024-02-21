from utils import print_5_executed_operations
import os


def make_path(file_name):
    if os.name == 'nt':
        path = '..\\data\\' + file_name
    else:
        path = '../data/' + file_name
    return path


def test_make_path():
    path = make_path('operations.json')
    assert print_5_executed_operations.make_path('operations.json') == path


def test_reading_file():
    ...



def test_reading():
    ...


def test_prepare_data():
    ...


def test_printing_data():
    ...


def test_main():
    ...
