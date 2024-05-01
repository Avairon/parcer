import argparse
import sys

def sort_data_by_type(input_file, output_path, file_prefix, append_mode, stats_type):
    integers_output = open(f'{output_path}/{file_prefix}integers.txt', 'a' if append_mode else 'w')
    floats_output = open(f'{output_path}/{file_prefix}floats.txt', 'a' if append_mode else 'w')
    strings_output = open(f'{output_path}/{file_prefix}strings.txt', 'a' if append_mode else 'w')

    integers_count = 0
    floats_count = 0
    strings_count = 0
    integers_data = []
    floats_data = []
    strings_data = []

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            try:
                number = int(line)

                integers_output.write(f'{number} ')
                integers_count += 1
                integers_data.append(number)
            except ValueError:
                try:
                    number = float(line)
                    floats_output.write(f'{number} ')
                    floats_count += 1
                    floats_data.append(number)
                except ValueError:
                    strings_output.write(f'{line} ')
                    strings_count += 1
                    strings_data.append(line)

    integers_output.close()
    floats_output.close()
    strings_output.close()

    if stats_type == 'f':
        if integers_count > 0:
            print(f"Integers - Count: {integers_count}, Min: {min(integers_data)}, Max: {max(integers_data)}, Sum: {sum(integers_data)}, Avg: {sum(integers_data) / integers_count}")
        if floats_count > 0:
            print(f"Floats - Count: {floats_count}, Min: {min(floats_data)}, Max: {max(floats_data)}, Sum: {sum(floats_data):.2f}, Avg: {sum(floats_data) / floats_count:.2f}")
    elif stats_type == 's':
        print(f"Integers - Count: {integers_count}")
        print(f"Floats - Count: {floats_count}")
        print(f"Strings - Count: {strings_count}")

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
