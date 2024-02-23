import os
import json


def make_path(filename):
    path = os.path.join('..', 'data', filename)
    return path


def reading_file(path):
    with open(path, "rt", encoding="utf-8") as file:
        raw_operations = file.read()
    return raw_operations


def making_list_from_json(raw_operations):
    operations = json.loads(raw_operations)
    return operations


def reading_operations_file(filename):
    path = make_path(filename)
    raw_operations = reading_file(path)
    operations = making_list_from_json(raw_operations)
    prepare_data(operations)


def prepare_data(operations):
    five_executed = []
    i = 0
    while len(five_executed) < 5:
        if len(operations) != 0:
            if operations[i]['state'] == "EXECUTED":
                five_executed.append(operations[i])
        i += 1
        if i >= len(operations):
            break
    return five_executed


def printing_data():
    ...


def main():
    reading_operations_file('operations.json')


main()