# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
            if "mode access" in line:
                vlans_on_int[0][interface] = 1
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

print(get_int_vlan_map('config_sw2.txt'))