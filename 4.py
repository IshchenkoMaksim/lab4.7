#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из однострочного и многострочного
текстовых полей и двух кнопок "Открыть" и "Сохранить".  При клике
на первую должен открываться на чтение файл, чье имя указано в поле
класса Entry, а содержимое файла должно загружаться в поле типа Text.
При клике на вторую кнопку текст, введенный пользователем в экземпляр
Text, должен сохраняться в файле под именем, которое пользователь указал
в однострочном текстовом поле. Файлы будут читаться и записываться в том
же каталоге, что и файл скрипта, если указывать имена файлов без адреса.
"""

from tkinter import Tk, Label, Button, END, Text, E, W
from tkinter import filedialog as fd


def open_file():
    text.delete(1.0, END)
    filename = fd.askopenfilename()
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            data = f.read()
        text.insert(1.0, data)
        lab['text'] = filename
    except FileNotFoundError:
        text.insert(1.0, 'Вы забыли выбрать файл')


def save_file():
    filename = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    data = text.get(1.0, END)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(data)
    lab['text'] = filename


if __name__ == '__main__':
    root = Tk()

    lab = Label(width=30)
    lab.grid(row=1, sticky=W)

    b1 = Button(text="Открыть", command=open_file)
    b1.grid(row=1, sticky=E)

    b2 = Button(text="Сохранить", command=save_file)
    b2.grid(row=1, column=1, sticky=W)

    text = Text(width=70, height=35)
    text.grid(columnspan=2)

    root.mainloop()
