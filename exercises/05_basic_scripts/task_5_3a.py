# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

port_mode = {'access': access_template, 'trunk': trunk_template}
vlan_in_welcome = {'access': 'Введите номер VLAN: ', 'trunk': 'Введите разрешенные VLANы: '}
port_mode_in = input('Введите режим работы интерфейса (access/trunk): ')
port_type_number_in = input('Введите тип и номер интерфейса: ')
vlan_in = input(vlan_in_welcome[port_mode_in])

port_type_number = 'interface {}\n'.format(port_type_number_in)

print(port_type_number + '\n'.join(port_mode[port_mode_in]).format(vlan_in))