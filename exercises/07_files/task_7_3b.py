# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

list = []
vlan_in = input("Введите номер vlan: ")

with open('CAM_table.txt') as f:
    for line in f:
        line_list = line.split()
        if len(line_list) > 1 and len(line_list[1]) == 14 and line_list[0] == vlan_in:
            list.append(line_list)

for line in list:
        line[0] = int(line[0])

list.sort()

for line in list:
        print('{:<9}{:20}{:10}'.format(line[0],line[1],line[3]))