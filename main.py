import argparse
import sys

def statistic(ints, floats, strings, type):
    if type == 'f':
        if len(ints) > 0:
            print(f"Integers - Count: {len(ints)}, Min: {min(ints)}, Max: {max(ints)}, Sum: {sum(ints)}, Avg: {sum(ints) / len(ints)}")
        if len(floats) > 0:
            print(f"Floats - Count: {len(floats)}, Min: {min(floats)}, Max: {max(floats)}, Sum: {sum(floats):.2f}, Avg: {sum(floats) / len(floats):.2f}")
    elif type == 's':
        print(f"Integers - Count: {len(ints)}")
        print(f"Floats - Count: {len(floats)}")
        print(f"Strings - Count: {len(strings)}")

def pars_to_files(input_file, output_path, file_prefix, append_mode, if_has):

    if(if_has[0] == 1):
        integers_output = open(f'{output_path}/output/{file_prefix}integers.txt', 'a' if append_mode else 'w')
    if(if_has[1] == 1):
        floats_output = open(f'{output_path}/output/{file_prefix}floats.txt', 'a' if append_mode else 'w')
    if(if_has[2] == 1):
        strings_output = open(f'{output_path}/output/{file_prefix}strings.txt', 'a' if append_mode else 'w')
    
    if(if_has[0] == 1 or if_has[1] == 1 or if_has[2] == 1):
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    number = int(line)
                    if(if_has[0] == 1):
                        integers_output.write(f'{number} ')
                except ValueError:
                    try:
                        number = float(line)
                        if(if_has[1] == 1):
                            floats_output.write(f'{number} ')
                    except ValueError:
                        if(if_has[2] == 1):
                            strings_output.write(f'{line} ')
    
    if(if_has[0] == 1):
        integers_output.close()
    if(if_has[1] == 1):
        floats_output.close()
    if(if_has[2] == 1):
        strings_output.close()    
    

def sort_data_by_type(input_file, output_path, file_prefix, append_mode, stats_type):

    integers_data = []
    floats_data = []
    strings_data = []

    if_has = [0, 0, 0]

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            try:
                number = int(line)
                integers_data.append(number)
            except ValueError:
                try:
                    number = float(line)
                    floats_data.append(number)
                except ValueError:
                    strings_data.append(line)

    if len(integers_data) > 0:
        if_has[0] = 1
    if len(floats_data) > 0:
        if_has[1] = 1
    if len(strings_data) > 0:
        if_has[2] = 1

    pars_to_files(input_file, output_path, file_prefix, append_mode, if_has)

    statistic(integers_data, floats_data, strings_data, stats_type)

    integers_data.clear()
    floats_data.clear()
    strings_data.clear()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('-o', '--output_path', help='Путь для сохранения результатов', default='./')
    parser.add_argument('-p', '--file_prefix', help='Префикс имен выходных файлов', default='')
    parser.add_argument('-a', '--append_mode', action='store_true', help='Режим добавления в существующие файлы')
    parser.add_argument('-s', '--stats_type', choices=['f', 's'], default='s', help='Тип статистики: краткая (s) или полная (f)')

    try:
        args = parser.parse_args()
        sort_data_by_type(args.input_file, args.output_path, args.file_prefix, args.append_mode, args.stats_type)
    except Exception as e:
        print(f'Произошла ошибка: {e}')