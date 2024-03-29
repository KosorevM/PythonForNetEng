# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re

regex_description = r'^ description'
regex_interface = r'^interface (\S+)'


def get_ints_without_description(file_name):
    result = list()
    with open(file_name, 'r') as file:
        for _ in file:
            if re.search(regex_interface, _):
                interface = re.search(regex_interface, _)
                if interface:
                    result.append(interface.group(1))
            match = re.search(regex_description, _)
            if match:
                result.remove(interface.group(1))
    return result


if __name__ == "__main__":
    print(get_ints_without_description("config_r1.txt"))