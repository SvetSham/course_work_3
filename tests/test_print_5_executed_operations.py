import pytest
from utils import print_5_executed_operations
import os


@pytest.fixture
def operations_list_of_dict_fixture():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]


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


def test_making_dict_from_json():
    ...


def test_prepare_data():
    ...


def test_printing_data():
    ...


def test_main():
    ...
