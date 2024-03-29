# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""

import re

regex = r'(\S+)\s+(\S+ \S+)\s+\d+\s+.*(\S{3,} \S+)\n$'

exceptions = ['show', 'Capability', 'IGMP', 'Intrfce']

def generate_description_from_cdp(file_name):
    result = dict()
    with open(file_name, 'r') as file:
        for _ in file:
            if ('show' in _) or (_ == "\n") or ('Capability' in _) or ('IGMP' in _) or ('Intrfce' in _) :
                continue
            if re.search(regex, _):
                interface = re.search(regex, _)
                print(interface.group(1), interface.group(2), interface.group(3))
                result[interface.group(2)] = f'description Connected to {interface.group(1)} port {interface.group(3)}'
    return result


if __name__ == "__main__":
    print(generate_description_from_cdp("sh_cdp_n_sw1.txt"))