# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_addr_in = input("Введите IP-адрес: ")
ip_addr_correct = False
counter = 0
while not ip_addr_correct:
    for symbol in ip_addr_in:
        if symbol == '.':
            counter += 1
    if counter != 3:
        count_check = False
        print('Неправильный IP-адрес')
        break
    else:
        ip_addr_octets = ip_addr_in.split('.')
        count_check = True
    for a in ip_addr_octets:
        if a.isdigit() == False or int(a) < 0 or int(a) > 255:
            digit_check = False
            break
        else:
            digit_check = True
    if len(ip_addr_octets) != 4:
        octets_check = False
        print('Неправильный IP-адрес')
        break
    else:
        octets_check = True
    if octets_check == True and digit_check == True and count_check == True:
        ip_addr_correct = True
        break
    print('Неправильный IP-адрес')
    break

if ip_addr_correct == True:
    if int(ip_addr_octets[0]) >= 1 and int(ip_addr_octets[0]) <= 223:
        print('unicast')
    elif int(ip_addr_octets[0]) >= 224 and int(ip_addr_octets[0]) <= 239:
        print('multicast')
    elif ip_addr_in == '255.255.255.255':
        print('local broadcast')
    elif ip_addr_in == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')