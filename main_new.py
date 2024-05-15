import argparse  # ДИСКЛЕЙМЕР можешь на картошку посадить все коменты, мне арбуз ваще
import sys
from dataclasses import dataclass
from typing import Union
import os

@dataclass
class Stats: #класс с насследованием, в нем статистика
    count_values: int = 0
    max: Union[int, float] = 0
    min: Union[int, float] = 99999999
    sum: Union[int, float] = 0

    def addval(self, value: Union[int, float]) -> None:
        self.count_values += 1
        if self.max < value:
            self.max = value
        if self.min > value:
            self.min = value
        self.sum += value

    #def __iadd__(self, value: Union[int, float]) -> None:
    #    self.count_values += 1
    #    if self.max < value:
    #        self.max = value
    #    if self.min > value:
    #        self.min = value
    #    self.sum += value

    @property
    def avg(self) -> float:
        return self.sum / self.count_values

#   stats = Stats()
#   stats + 10
#   stats.avg

def statistic(ints, floats, strings, type):
    if type == 'f':
        if ints.count_values > 0:
            print(f"Integers - Count: {ints.count_values}, Min: {ints.min}, Max: {ints.max}, Sum: {ints.sum}, Avg: {ints.sum / ints.count_values}")
        if floats.count_values > 0:
            print(f"Floats - Count: {floats.count_values}, Min: {floats.min}, Max: {floats.max}, Sum: {floats.sum:.2f}, Avg: {floats.sum / floats.count_values:.2f}")
        if strings.count_values > 0:
            print(f"Strings - Count: {strings.count_values}, Min length: {strings.min}, Max length: {strings.max}, Sum of lengths: {strings.sum}, Avg length: {strings.sum / strings.count_values:.2f}")
    elif type == 's':
        print(f"Integers - Count: {ints.count_values}")
        print(f"Floats - Count: {floats.count_values}")
        print(f"Strings - Count: {strings.count_values}")
    

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
                int_stats.addval(int_)
                save(0, int_)
            except ValueError:
                try:
                    float_ = float(line)
                    float_stats.addval(float_)
                    save(1, float_)
                except ValueError:
                    string_ = line
                    string_stats.addval(len(string_))
                    save(2, string_)

    statistic(int_stats, float_stats, string_stats, stats_type)

    # А тут можешь просто выдавать статистику через все переменные внутри обьекта

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
