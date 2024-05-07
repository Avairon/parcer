# File_sys_python
1. Function:
- sort_data_by_type: Read data and check type (Int, float or str) and write in output files.

2. Code:
- Create parser with help argparse.
- User can use Flags:
-o (Path the save result)
-p (Name output files).
-a (Append mode)
-s (To check statistic)
- Call the func sort_data_by_type, give a file and flags result.

3. Function sort_data_by_type:
- Open "input file" and create output files.
- Read all lines from file.
- Try to convert int(). If convert, write to Integer output file.
- If not convert, try convert to float(). If convert, write to Float output file.
- If not convert, write to String output file.
- Close all files.

# For run code use
**python Main.py input_file.txt**
- Can add flags:
-p Name_file
-o Path_to_save
-a Append mode
-s ('f' - Full stats, 's' - short stats) To check statistic


## Review

1. Использование списков
   ```
   integers_data = []
   floats_data = []
   strings_data = []
   ```

>  > вопрос? зачем? а если у вас будет очень много файлов, а в них будет очень много значений, то тогда вы просто их все не сможете сохранить в оперативной памяти. Соответственно, для того, чтобы вести статистику вам бы хватило 6 перменных для числовых типов данных (данные не нужно хранить в памяти!!!!) и 2 значений для стрингов.

2. Зачем создавать 3 переменные для int_count, float_cout, string_cout, когда можно было бы просто создать класс `Stats` в этом классе определить переменную count, метод для инкремента этой переменной, а дальше расширять класс Stats двумя другими классами - NumericStats и StringStats. Уже внутри этих классов можно было бы вести статистику по каждому типу. count инкрементировался бы путем наследования реализации от класса Stats. Остальные переменные (поля класса) уже как то по другому вычислялись для каждого объекта класса.
3. Мне не нравится реализация для статистики. а если у нас еще добавятся типы данных - будешь в коде фрагментарно вставлять код? вместо того, чтобы реализовать класс для нового типа данных и просто создать потом в коде объект этого класса и как то с ним уже взаимодействовать. Также можно в классах определить реализацию для общих методов (например printFullStats или printShortStats)
4. Декомпозиции 0. Одна громадная функция, которая делает все.
5. Косяк в том, что при отсутствии типа данных какого-то у вас все равно создается файл с результатами.
