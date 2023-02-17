from pandas import read_excel


class ДескрипторВысотаШирина:

    @staticmethod
    def проверить_входное_число(x):
        if not type(x) in (int, float):
            raise ValueError("Необходимо передать число")

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.проверить_входное_число(value)
        if hasattr(instance, self.name):
            if value <= instance.__dict__[self.name]:
                instance.__dict__[self.name] = value
            else:
                raise ValueError("Нельзя увеличить высоту и ширину таблицы")
        else:
            instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class СырыеДанные:
    """Класс для считывания исходных данных с минимальной их обработкой"""

    breadth = ДескрипторВысотаШирина()
    height = ДескрипторВысотаШирина()

    def __init__(self, path_to_file, sheet_name, keys_list):
        """конструктор объекта"""
        self.__data = read_excel(path_to_file, sheet_name=sheet_name)
        self.height = len(self.__data)
        self.breadth = len(self.__data.columns)
        self.__keys = {}
        for word in keys_list:
            self.__keys[word] = []
        for x in range(self.height):
            for y in range(self.breadth):
                for word in keys_list:
                    if self.__data.iloc[x, y] == word:
                        self.__keys[word].append([x, y])
                        break
        self.not_found = None
        for word in self.__keys.keys():
            if not self.__keys[word]:
                if not self.not_found:
                    self.not_found = word
                else:
                    self.not_found += ", " + word

    @property
    def keys(self):
        return self.__keys

    @keys.deleter
    def keys(self):
        del self.__keys

    @property
    def data(self):
        return self.__data
