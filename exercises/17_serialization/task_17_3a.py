# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import yaml
def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    result_dict = {}
    for file in list_of_files:
        with open(file) as f:
            f=f.read()
            for line in f.split("\n"):
                if ">" in line:
                    hostname = line.split(">")[0]
                if "/" in line:
                    local_intf = line.split()[1] + " " + line.split()[2]
                    remote_hostname = line.split()[0]
                    remote_intf = line.split()[-2] + " " + line.split()[-1]
                    result_dict.setdefault(hostname, {})[local_intf] = {remote_hostname: remote_intf}
    if save_to_filename:
        with open(save_to_filename, "w") as f:
            f.write(yaml.dump(result_dict))
    return result_dict


if __name__ == "__main__":
    topology = generate_topology_from_cdp(["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt",
                                           "sh_cdp_n_r3.txt", "sh_cdp_n_r4.txt", "sh_cdp_n_r5.txt",
                                           "sh_cdp_n_r6.txt"])