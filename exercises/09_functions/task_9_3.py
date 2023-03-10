# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        vlans_on_int = ({},{})
        interface = ''
        for line in f:
            line_list = line.split()
            if "interface" in line_list:
                interface = line_list[1]
            if "access vlan" in line:
                vlans_on_int[0][interface] = int(line_list[3])
            if "trunk allowed" in line:
                    a = line_list[4].split(',')
                    c = []
                    for b in a:
                        b = int(b)
                        c.append(b)
                    vlans_on_int[1][interface] = c
    return vlans_on_int
print(get_int_vlan_map('config_sw1.txt'))