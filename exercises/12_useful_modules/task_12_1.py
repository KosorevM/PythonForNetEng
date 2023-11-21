# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
list_of_addresses = ("10.100.9.254", "8.8.8.8")
ip_address_dostupni = []
ip_address_ne_dostupni = []
def ping_ip_addresses(input_list):
    for _ in input_list:
        result = subprocess.run(['ping', '-c', '1', _], stdout=subprocess.DEVNULL)
        ip_address_dostupni.append(_) if result.returncode == 0 else ip_address_ne_dostupni.append(_)
    final_tuple = ip_address_dostupni, ip_address_ne_dostupni
    return(final_tuple)

if __name__ == "__main__":
    print(ping_ip_addresses(list_of_addresses))