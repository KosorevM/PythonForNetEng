# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
import tabulate


def print_ip_table(reachable, not_reachable):
    my_tuple = dict(Reachable=reachable, Unreachable=not_reachable)
    print(tabulate.tabulate(my_tuple, headers='keys'))


list_reachable = ["10.10.1.7", "10.10.1.8", "10.10.1.9", "10.10.1.15"]
list_not_reachable = ["10.1.1.7", "10.1.1.8"]

if __name__ == "__main__":
    print_ip_table(list_reachable, list_not_reachable)
