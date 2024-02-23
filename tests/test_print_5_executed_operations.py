import pytest
from utils import print_5_executed_operations
import os

OPERATIONS_FILE_NAME = 'operations.json'

TEXT_OPERATIONS = """[
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
]"""


@pytest.fixture
def operations_list_fixture():
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


LIST1_TASK = [
        {'num': 0, 'state': 'EXECUTED'},
        {'num': 1, 'state': 'EXECUTED'},
        {'num': 2, 'state': 'CANCELED'},
        {'num': 3, 'state': 'EXECUTED'},
        {'num': 4, 'state': 'EXECUTED'},
        {'num': 5, 'state': 'EXECUTED'}
    ]

LIST1_ANSWER = [
        {'num': 0, 'state': 'EXECUTED'},
        {'num': 1, 'state': 'EXECUTED'},
        {'num': 3, 'state': 'EXECUTED'},
        {'num': 4, 'state': 'EXECUTED'},
        {'num': 5, 'state': 'EXECUTED'}
    ]

LIST2_TASK = [
        {'num': 0, 'state': 'CANCELED'},
        {'num': 1, 'state': 'CANCELED'},
        {'num': 2, 'state': 'CANCELED'},
        {'num': 3, 'state': 'EXECUTED'},
        {'num': 4, 'state': 'EXECUTED'},
        {'num': 5, 'state': 'EXECUTED'}
    ]

LIST2_ANSWER = [
        {'num': 3, 'state': 'EXECUTED'},
        {'num': 4, 'state': 'EXECUTED'},
        {'num': 5, 'state': 'EXECUTED'}
    ]

LIST3_TASK = []
LIST3_ANSWER = []


def make_path_for_test(file_name):
    if os.name == 'nt':
        path = '..\\data\\' + file_name
    else:
        path = '../data/' + file_name
    return path


def test_make_path():
    path = make_path_for_test(OPERATIONS_FILE_NAME)
    assert print_5_executed_operations.make_path(OPERATIONS_FILE_NAME) == path


def test_reading_file():
    assert print_5_executed_operations.reading_file('for_course_3.json') == TEXT_OPERATIONS


def test_reading_file__file_not_found():
    with pytest.raises(FileNotFoundError):
        print_5_executed_operations.reading_file('operations')


def test_making_list_from_json(operations_list_fixture):
    assert print_5_executed_operations.making_list_from_json(TEXT_OPERATIONS) == operations_list_fixture


def test_prepare_data():
    assert print_5_executed_operations.prepare_data(LIST1_TASK) == LIST1_ANSWER
    assert print_5_executed_operations.prepare_data(LIST2_TASK) == LIST2_ANSWER
    assert print_5_executed_operations.prepare_data(LIST3_TASK) == LIST3_ANSWER



def test_printing_data():
    ...


def test_main():
    ...
