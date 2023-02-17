from pandas import ExcelWriter


class Печать:

    def _стиль(self, табл):
        def style_all(v, props=''):
            return props
        times_new_roman = 'font-family: "Times New Roman", Times, serif;'
        font_size = 'font-size:1em;'
        horizontal = 'text-align:center;'
        vertical = 'vertical-align:middle;'
        all_cells = (times_new_roman + font_size +
                     horizontal + vertical)
        not_all_cells = (times_new_roman + font_size +
                         vertical + 'text-align:left:')
        стилизовано = (
            табл.style.applymap(style_all, props=all_cells)
            .applymap(style_all, props=not_all_cells,
                      subset=[self._шапка[self._особ_столбцы[0]],
                              self._шапка[self._особ_столбцы[1]]])
        )
        return стилизовано

    @staticmethod
    def печать(writer, data_dict):
        for k, v in data_dict.items():
            v.to_excel(writer, sheet_name=k)

    def __init__(self, path, название_файла, шапка, номера_особенных_столбцов):
        self._файл = название_файла
        self._особ_столбцы = номера_особенных_столбцов
        self._шапка = шапка
        self._путь = path

    def __call__(self, table_to_xls=None, dict_to_xls=None):
        if not isinstance(table_to_xls, type(None)):
            xls = {"материалы": self._стиль(table_to_xls)}
        else:
            xls = {}
        if not isinstance(dict_to_xls, type(None)):
            dict_xls = {}
            for k, v in dict_to_xls.items():
                dict_xls[k] = self._стиль(v)
        else:
            dict_xls = {}
        writer = ExcelWriter(self._путь+"/"+self._файл)
        self.печать(writer, xls)
        self.печать(writer, dict_xls)
        writer.save()
