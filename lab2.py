import csv
import datetime


def start():
    records = readfile('test-file.csv')
    console_result = console()
    while console_result != '0':
        if console_result == '1':
            print('Список всех отделов:')
            for department in records.keys():
                print(f'{department}')
        elif console_result == '2':
            for report in gen_report(records):
                print(report)
        elif console_result == '3':
            file_name = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.csv')}"
            report_file = open(file_name, 'w')
            for report in gen_report_csv(records):
                report_file.write(report)
            report_file.close()
            print(f'Выгрузка отчетов в файл {file_name} завершена.')
        console_result = console()


def gen_report(divisions):
    """Сгенерировать отчет"""
    my_report = []
    for key in divisions:
        payments = [int(item) for item in divisions.get(key)]
        my_report.append(f"Отдел {key}\n"
                         f"_________________\n"
                         f"Численность: {len(payments)}\n"
                         f"Зарплата: {min(payments)} ₽ - {max(payments)} ₽\n"
                         f"Средняя зарпалата: {sum(payments) // len(payments)} ₽\n")
    return my_report


def gen_report_csv(divisions):
    """Сгенерировать отчет в формате csv"""
    my_report = []
    for key in divisions:
        payments = [int(item) for item in divisions.get(key)]
        my_report.append(f"{key},{len(payments)},{min(payments)},{max(payments)},{sum(payments) // len(payments)}\n")
    return my_report


def readfile(file_name: str):
    """Прочитать из файла с именем file_name"""
    csvfile = open(file_name, encoding='utf8')
    reader = csv.reader(csvfile)
    result = {}
    for row in reader:
        if result.get(row[2]) is None:
            d = {row[2]: [row[4]]}
            result.update(d)
        else:
            result.get(row[2]).append(row[4])
    return result


def console():
    """Считать из консоли правильные команды"""
    print(
        '1 - Вывести все отделы\n'
        '2 - Вывести сводный отчёт по отделам\n'
        '3 - Сохранить сводный отчёт в виде csv\n'
        '0 - Выход'
    )
    option = ''
    options = {'1': '1', '2': '2', '3': '3', '0': '0'}
    while option not in options:
        option = input('Введите вариант ({}, {}, {}, {}): '.format(*options))
        if option not in options:
            print('Команда {} не поддерживается.'.format(option))
    return options[option]


if __name__ == "__main__":
    start()
