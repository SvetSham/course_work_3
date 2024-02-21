from utils import print_5_executed_operations
import os


def test_make_path():
    if os.name == 'nt':
        path = '..\data\operations.json'
    else:
        path = '../data/operations.json'
    assert print_5_executed_operations.make_path('operations.json') == path

def test_reading():
    ...


def test_prepare_data():
    ...


def test_printing_data():
    ...


def test_main():
    ...
