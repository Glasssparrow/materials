from pandas import DataFrame


class ФормированиеТаблицы:
    """Класс формирующий таблицу pandas при помощи которой будет \
    выполняться печать"""

    def _создать_таблицу(self, словарь):
        xls = DataFrame()
        for колонка in self._шапка:
            xls.loc["Позиция", колонка] = колонка
        for k, v in словарь.items():
            for x in self._номера:
                xls.loc[k, self._шапка[x]] = v
        xls.drop(labels=["Позиция"], inplace=True)
        return xls

    def _создать_словарь_таблиц(self, словари_в_словаре):
        таблицы = {}
        for k, v in словари_в_словаре.items():
            таблицы[k] = self._создать_таблицу(v)
        return таблицы

    def __init__(self, шапка_таблицы, лист_номеров_заполняемых_элементов):
        self._шапка = шапка_таблицы
        self._номера = лист_номеров_заполняемых_элементов

    def __call__(self, материалы_всё, материалы_части):
        self._xls = self._создать_таблицу(материалы_всё)
        self._few_xls = self._создать_словарь_таблиц(материалы_части)

    @property
    def one(self):
        return self._xls

    @property
    def multiple(self):
        return self._few_xls
