import os
import json
import datetime


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


def reading_data(operation_datetime: str) -> str:
    """Transformation datetime to date in mask dd.mm.yyyy"""
    if operation_datetime != '':
        full_datetime = datetime.datetime.strptime(operation_datetime, '%Y-%m-%dT%H:%M:%S.%f')
        operation_date = full_datetime.strftime('%d.%m.%Y')
        return operation_date
    else:
        return ''


def get_from_num(card_from: str) -> str:
    card_list = card_from.split(' ')
    return card_list[-1]


def get_from_name(card_from: str) -> str:
    card_list = card_from.split(' ')
    card_name_list = card_list[0: -1]
    card_name = ' '.join(card_name_list)
    return card_name


def mask_card_num(card_from_num: str) -> str:
    if card_from_num != "":
        masked_card_num = list(card_from_num)

        for i in range(6,len(card_from_num)-4):
            masked_card_num[i] = '*'

        for i in range(4, len(card_from_num), 5):
            masked_card_num.insert(i, ' ')

        masked_card_num = ''.join(masked_card_num)

        return masked_card_num
    else:
        return ""


def mask_account_num(account_to_num):
    if account_to_num != '':
        masked_account_num = '**' + account_to_num[-4:]
        return masked_account_num
    else:
        return ''


def printing_data(five_executed):
    for i in range(len(five_executed)):
        data = reading_data(five_executed[i]["date"])
        description = five_executed[i]["description"]
        if 'from' in list(five_executed[i]):
            card_from_num = get_from_num(five_executed[i]["from"])
            card_from_num = mask_card_num(card_from_num)
            card_from_name = get_from_name(five_executed[i]["from"])
        else:
            card_from_num = '???'
            card_from_name = '???'
        account_to_name = get_from_name(five_executed[i]["to"])
        account_to_num = get_from_num(five_executed[i]["to"])
        account_to_num = mask_account_num(account_to_num)
        amount = five_executed[i]["operationAmount"]["amount"]
        currency = five_executed[i]["operationAmount"]["currency"]["name"]

        print(data, description)
        print(card_from_name, card_from_num, '->', account_to_name, account_to_num)
        print(amount, currency)
        print()
    return True


def main():
    path = make_path('operations.json')
    raw_operations = reading_file(path)
    operations = making_list_from_json(raw_operations)
    five_executed = prepare_data(operations)
    printed = printing_data(five_executed)


main()
