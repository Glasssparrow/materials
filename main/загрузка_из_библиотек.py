from pandas import read_excel
from pandas import DataFrame


class Библиотека:

    def _загрузить_библиотеку(self, path, sheet, колонка_имен):
        try:
            library = read_excel(path, sheet_name=sheet)
            library.index = library[колонка_имен]
            library.pop(колонка_имен)
            return library
        except FileNotFoundError:
            self._предупреждения = "Не найден файл библиотеки"
        except ValueError:
            self._предупреждения = "Не найден лист библиотеки"
        library = DataFrame()
        for x in self._шапка:
            library.loc["Библиотека пуста", x] = 0
        return library

    @staticmethod
    def _сортировка(table):
        return table.sort_index()

    # Эту функцию стоит переписать.
    # Стоит попробовать получить строку из библиотеки методом get
    # Таким образом можно избавиться от конструкции try-except
    def _основная_функция(self, data):
        for номер in self._номера:
            for материал in data.index.tolist():
                try:
                    data.loc[материал, self._шапка[номер]] = (
                        self._библиотека.loc[материал, self._шапка[номер]]
                    )
                except:
                    continue
        data = self._сортировка(data)
        return data

    def _заполнение_словаря(self, словарь_таблиц):
        result = {}
        for k, v in словарь_таблиц.items():
            result[k] = self._основная_функция(v)
        return result

    def _найти_недостающее(self, data):
        удалить = []
        if self._нет_в_библ:
            for x in range(len(self._нет_в_библ)):
                if self._нет_в_библ[x] in self._библиотека.index:
                    удалить.append(x)
            удалить.sort(reverse=True)
            for number in удалить:
                del self._нет_в_библ[number]
        else:
            self._нет_в_библ = []
            for x in data.index.tolist():
                if x not in self._библиотека.index.tolist():
                    self._нет_в_библ.append(x)

    def _найти_недостающее_для_словаря(self, словарь):
        for k, v in словарь.items():
            self._найти_недостающее(v)

    def __init__(self, шапка_таблицы, лист_ном_зап_кол, колонка_имен):
        self._шапка = шапка_таблицы
        self._номера = лист_ном_зап_кол
        self._библ_имена = колонка_имен

    def __call__(self, path_to_library, sheet_name, data=None,
                 словарь_таблиц=None, нет_в_библ=None):
        self._предупреждения = "Порядок"
        self._нет_в_библ = нет_в_библ
        self._библиотека = self._загрузить_библиотеку(path_to_library,
                                                      sheet_name,
                                                      self._библ_имена)
        if not isinstance(data, type(None)):
            self._результат = self._основная_функция(data)
            self._найти_недостающее(data)
        else:
            self._результат = None
        if not isinstance(словарь_таблиц, type(None)):
            self._словарь = self._заполнение_словаря(словарь_таблиц)
            self._найти_недостающее_для_словаря(словарь_таблиц)
        else:
            self._словарь = None

    @property
    def one(self):
        if not isinstance(self._результат, type(None)):
            return self._результат
        else:
            raise ValueError("Нет таблицы данных "
                             "Вероятно, она не была подана при вызове")

    @property
    def multiple(self):
        if not isinstance(self._словарь, type(None)):
            return self._словарь
        else:
            raise ValueError("Нет словаря с таблицами. "
                             "Вероятно, он не был подан при вызове")

    @property
    def not_in_lib(self):
        return self._нет_в_библ

    @property
    def warnings(self):
        return self._предупреждения
