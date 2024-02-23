import pytest
from src import print_5_executed_operations
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


def test_make_path():
    if os.name == 'nt':
        path = '..\\data\\' + OPERATIONS_FILE_NAME
    else:
        path = '../data/' + OPERATIONS_FILE_NAME
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


def test_reading_data():
    assert print_5_executed_operations.reading_data("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert print_5_executed_operations.reading_data("") == ""


def test_get_from_num():
    assert print_5_executed_operations.get_from_num("Счет 48894435694657014368") == '48894435694657014368'
    assert print_5_executed_operations.get_from_num("Visa Classic 6831982476737658") == '6831982476737658'
    assert print_5_executed_operations.get_from_num("") == ''


def test_get_from_name():
    assert print_5_executed_operations.get_from_name("Счет 48894435694657014368") == "Счет"
    assert print_5_executed_operations.get_from_name("Visa Classic 6831982476737658") == "Visa Classic"
    assert print_5_executed_operations.get_from_name("") == ""


def test_mask_card_num():
    assert print_5_executed_operations.mask_card_num("48894435694657014368") == "4889 44** **** **** 4368"
    assert print_5_executed_operations.mask_card_num("6831982476737658") == "6831 98** **** 7658"
    assert print_5_executed_operations.mask_card_num("") == ""


def test_mask_account_num():
    assert print_5_executed_operations.mask_account_num('64686473678894779589') == "**9589"
    assert print_5_executed_operations.mask_account_num('8990922113665229') == "**5229"
    assert print_5_executed_operations.mask_account_num('') == ""

