# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re

regex_ip_mask = r'ip address ((?:\d+.){1,3}\d+) ((?:\d+.){1,3}\d+)'
regex_interface = r'interface (\S+)'


def get_ip_from_cfg(file_name):
    result = dict()
    with open(file_name, 'r') as file:
        for _ in file:
            if re.search(regex_interface, _):
                interface = re.search(regex_interface, _).group(1)
            match = re.search(regex_ip_mask, _)
            if match:
                match = match.group(1, 2)
                if interface in result:
                    result[interface] += [match]
                else:
                    result[interface] = [match]
    return result


if __name__ == "__main__":
    print(get_ip_from_cfg("config_r2.txt"))