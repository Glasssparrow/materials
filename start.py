from interface.interface import Gui

исходные_данные = {
    "название_итогового_файла": "Материалы.xlsx",
    "path_to_file": "Спецификация.xlsx",
    "path_to_folder": "D:/работа/проекты текущие/",
    "path_to_library": 'library/Библиотека.xlsx',
    "main_library_sheet": "Материалы",
    "local_library_sheet": "Библиотека",
    "sheet_name": "Узлы",
    "метка_список": "KEY",
    "метка_узел": "key",
    "метка_вложенный_узел": "subnode",
    "шапка_таблицы": ["Наименование", "Обозначение", "Код", "Производитель",
                      "Единица измерения", "Количество",
                      "Масса", "Примечание"],
    "список_колонок_из_библиотеки": [0, 1, 2, 3, 4, 6, 7],
    "название_колонки_имен_библиотеки": 0,
    "номер_колонки_количества": 5
    }

gui = Gui(исходные_данные)
