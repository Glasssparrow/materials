import tkinter as tk
from tkinter import filedialog as fd
from interface.основной_расчет import Расчет


class Gui:
    placeholder_text = (
        "Здесь\nбудет\nсписок\n"
        "материалов\nкоторые\nотсутствуют\nв библиотеке"
    )
    title_text = "Потом придумаю"

    @staticmethod
    def _cut_filename(path_to_file):
        split = path_to_file.split("/")
        delete = len(split[len(split)-1])+1
        return path_to_file[:-delete]

    def _расчет(self):
        расчет = Расчет(self._исходные_данные)
        нет_в_библ = расчет()
        текст = ""
        for x in нет_в_библ:
            текст += x + "\n"
        self._показать_недостающее.configure(text=текст)

    def _filename(self):
        self._исходные_данные["path_to_file"] = (
            fd.askopenfilename(title="Выберите файл",
                               initialdir=(
                                   self._исходные_данные["path_to_folder"])
                               )
        )
        self._показать_путь_к_файлу.configure(
            text=self._исходные_данные["path_to_file"]
        )
        self._исходные_данные["path_to_folder"] = (
            self._cut_filename(self._исходные_данные["path_to_file"])
        )
        self._показать_путь_к_папке.configure(text=(
            self._исходные_данные["path_to_folder"])
        )

    def _folder(self):
        self._исходные_данные["path_to_folder"] = (
            fd.askdirectory(title="Открыть папку",
                            initialdir=self._исходные_данные["path_to_folder"])
        )
        self._показать_путь_к_папке.configure(text=(
            self._исходные_данные["path_to_folder"])
        )

    def __init__(self, исходные_данные):
        self._исходные_данные = исходные_данные
        self._window = tk.Tk()

        self._window.title(self.title_text)
        self._показать_недостающее = tk.Label(
            text=self.placeholder_text
        )
        self._показать_недостающее.pack(side="right")
        self._кнопка_выбора_файла = (
            tk.Button(self._window, text="Выбрать файл",
                      command=self._filename)
        )
        self._кнопка_выбора_файла.pack()
        self._показать_путь_к_файлу = (
            tk.Label(text=исходные_данные["path_to_file"]))
        self._показать_путь_к_файлу.pack(fill="both")
        self._кнопка_выбора_папки = (
            tk.Button(self._window, text="Выбрать папку",
                      command=self._folder)
        )
        self._кнопка_выбора_папки.pack()
        self._показать_путь_к_папке = (
            tk.Label(text=исходные_данные["path_to_folder"]))
        self._показать_путь_к_папке.pack(fill="both")
        self._выполнить_расчет = (
            tk.Button(self._window, text="Выполнить расчет",
                      command=self._расчет)
        )
        self._выполнить_расчет.pack()
        self._window.mainloop()
