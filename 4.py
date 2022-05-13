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

from tkinter import Tk, Entry, Button, LEFT, END, Text, Frame


def open_file(event):
    text.delete(1.0, END)
    try:
        filename = ent.get()
        with open(filename, 'r', encoding="utf-8") as f:
            data = f.read()
        text.insert(1.0, data)
    except FileNotFoundError:
        text.insert(1.0, 'Вы забыли указать имя файла, '
                         'или такого файла не существует')


def save_file(event):
    filename = ent.get()
    data = text.get(1.0, END)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__':
    root = Tk()

    frame = Frame()
    frame.pack()

    ent = Entry(frame, width=30)
    ent.pack(side=LEFT)

    but1 = Button(frame, text='Открыть', width=8, pady=5)
    but1.bind('<Button-1>', open_file)
    but1.pack(side=LEFT)

    but2 = Button(frame, text='Сохранить', width=8, pady=5)
    but2.bind('<Button-1>', save_file)
    but2.pack()

    text = Text(width=70, height=35)
    text.pack()

    root.mainloop()
