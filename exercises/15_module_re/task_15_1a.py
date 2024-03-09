# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
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
                interface = re.search(regex_interface, _)
            match = re.search(regex_ip_mask, _)
            if match:
                result[interface.group(1)] = match.group(1, 2)
    return result


if __name__ == "__main__":
    print(get_ip_from_cfg("config_r1.txt"))
