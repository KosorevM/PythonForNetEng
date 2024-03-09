# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""

import re

regex = r'([FL]\S+)\s+(\S+)(?:\s+\S+){2}\s+(\S+(?:\s\S+)?)\s+(\S+)'


def parse_sh_ip_int_br(file_name):
    result = list()
    with open(file_name, 'r') as file:
        for _ in file:
            match = re.search(regex, _)
            if match:
                result.append(match.group(1, 2, 3, 4))
    return result


if __name__ == "__main__":
    print(parse_sh_ip_int_br("sh_ip_int_br.txt"))