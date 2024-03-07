# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress


def convert_ranges_to_ip_list(ip_list):
    result = []

    for ip_entry in ip_list:
        if '-' in ip_entry:
            start_ip, end_ip = ip_entry.split('-')
            start_parts = start_ip.split('.')
            end_parts = end_ip.split('.')

            if len(end_parts) == 1:
                # If the end IP is in the form of a single octet, append it to the start IP
                end_parts = start_parts[:-1] + [end_parts[0]]

            start_octet = int(start_parts[3])
            end_octet = int(end_parts[3]) + 1  # Add 1 to include the end IP in the range

            for octet in range(start_octet, end_octet):
                result.append('.'.join(start_parts[:-1] + [str(octet)]))
        else:
            result.append(ip_entry)

    return result


# Пример использования:
ip_addresses = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

result_ip_list = convert_ranges_to_ip_list(ip_addresses)
print(result_ip_list)

if __name__ == "__main__":
    convert_ranges_to_ip_list(ip_addresses)
