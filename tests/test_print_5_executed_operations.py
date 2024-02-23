import pytest

from utils import print_5_executed_operations
import os


def make_path_for_test(file_name):
    if os.name == 'nt':
        path = '..\\data\\' + file_name
    else:
        path = '../data/' + file_name
    return path


def test_make_path():
    path = make_path_for_test('operations.json')
    assert print_5_executed_operations.make_path('operations.json') == path


def test_reading_file():
    with open('for_course_3.json', 'rt', encoding='utf-8') as file:
        test_raw_json = file.read()
    assert print_5_executed_operations.reading_file('for_course_3.json') == test_raw_json


def test_reading_file__file_not_found():
    with pytest.raises(FileNotFoundError):
        print_5_executed_operations.reading_file('operations')


def test_prepare_data():
    ...


def test_printing_data():
    ...


def test_main():
    ...
