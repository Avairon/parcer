import argparse  # ДИСКЛЕЙМЕР можешь на картошку посадить все коменты убрать, мне арбуз ваще
import sys
from dataclasses import dataclass
from typing import Union

@dataclass
class Stats: #класс с насследованием, в нем статистика
    count_values: int = 0
    max: Union[int, float] = 0
    min: Union[int, float] = 0
    sum: Union[int, float] = 0

    def __iadd__(self, value: Union[int, float]) -> None:
        self.count_values += 1
        if self.max < value:
            self.max = value
        if self.min > value:
            self.min = value
        self.sum += value

    @property
    def avg(self) -> float:
        return self.sum / self.count_values

#   stats = Stats()
#   stats + 10
#   stats.avg

#def statistic(ints, floats, strings, type):
#    if type == 'f':
#        if len(ints) > 0:
#            print(f"Integers - Count: {len(ints)}, Min: {min(ints)}, Max: {max(ints)}, Sum: {sum(ints)}, Avg: {sum(ints) / len(ints)}")
#        if len(floats) > 0:
#            print(f"Floats - Count: {len(floats)}, Min: {min(floats)}, Max: {max(floats)}, Sum: {sum(floats):.2f}, Avg: {sum(floats) / len(floats):.2f}")
#    elif type == 's':
#        print(f"Integers - Count: {len(ints)}")
#        print(f"Floats - Count: {len(floats)}")
#        print(f"Strings - Count: {len(strings)}")

#def pars_to_files(input_file, output_path, file_prefix, append_mode, if_has):
#
#    if(if_has[0] == 1):
#        integers_output = open(f'{output_path}/output/{file_prefix}integers.txt', 'a' if append_mode else 'w')
#    if(if_has[1] == 1):
#        floats_output = open(f'{output_path}/output/{file_prefix}floats.txt', 'a' if append_mode else 'w')
#    if(if_has[2] == 1):
#        strings_output = open(f'{output_path}/output/{file_prefix}strings.txt', 'a' if append_mode else 'w')
#
#    if(if_has[0] == 1 or if_has[1] == 1 or if_has[2] == 1):
#        with open(input_file, 'r') as file:
#            for line in file:
#                line = line.strip()
#                try:
#                    number = int(line)
#                    if(if_has[0] == 1):
#                        integers_output.write(f'{number} ')
#                except ValueError:
#                    try:
#                        number = float(line)
#                        if(if_has[1] == 1):
#                            floats_output.write(f'{number} ')
#                    except ValueError:
#                        if(if_has[2] == 1):
#                            strings_output.write(f'{line} ')
#
#    if(if_has[0] == 1):
#        integers_output.close()
#    if(if_has[1] == 1):
#        floats_output.close()
#    if(if_has[2] == 1):
#        strings_output.close()
    

def save(flag: int, data) -> None:
    files = [
        "integers.txt",
        "floats.txt",
        "strings.txt",
    ]
    with open(f"output/{files[flag]}", "a+") as f:
        f.write(f"{data}\n")


def sort_data_by_type(input_file, output_path, file_prefix, append_mode, stats_type):

#    integers_data = []
#    floats_data = []
#    strings_data = []

#    int_count = 0
#    float_count = 0
#    string_count = 0

    int_stats = Stats() # 3 класса со статистикой
    float_stats = Stats()
    string_stats = Stats()

    if_has = [0, 0, 0]

    with open(input_file, 'r') as file: # сам парсинг с записью если есть что
        for line in file:
            line = line.strip()
            try:
                int_ = int(line)
                int_stats += int_
                save(0, int_)
            except ValueError:
                try:
                    float_ = float(line)
                    float_stats += float_
                    save(1, float_)
                except ValueError:
                    string_ = line
                    string_stats += len(string_)
                    save(2, string_)

    if int_stats.count_values:
        if_has[0] = 1
    if float_stats.count_values:
        if_has[1] = 1
    if string_stats.count_values:
        if_has[2] = 1

    # А тут можешь просто выдавать статистику через все переменные внутри обьекта


   #pars_to_files(input_file, output_path, file_prefix, append_mode, if_has)

#   statistic(integers_data, floats_data, strings_data, stats_type)

#   integers_data.clear()
#   floats_data.clear()
#   strings_data.clear()



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
