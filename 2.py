#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из семи кнопок, цвета которых
соответствуют цветам радуги. При нажатии на ту или иную кнопку
в текстовое поле должен вставляться код цвета, а в метку – название
цвета. Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный,
#ff7d00 – оранжевый, #ffff00 – желтый, #00ff00 – зеленый,
#007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.
"""

from tkinter import Tk, Entry, Button, Label, END


def red(event):
    ent.delete(0, END)
    lab['text'] = "Красный"
    ent.insert(0, "#ff0000")


def orange(event):
    ent.delete(0, END)
    lab['text'] = 'Оранжевый'
    ent.insert(0, "#ff7d00")


def yellow(event):
    ent.delete(0, END)
    lab['text'] = 'Жёлтый'
    ent.insert(0, "#ffff00")


def green(event):
    ent.delete(0, END)
    lab['text'] = 'Зелёный'
    ent.insert(0, "#00ff00")


def cyan(event):
    ent.delete(0, END)
    lab['text'] = 'Голубой'
    ent.insert(0, "#007dff")


def blue(event):
    ent.delete(0, END)
    lab['text'] = 'Синий'
    ent.insert(0, "#0000ff")


def violet(event):
    ent.delete(0, END)
    lab['text'] = 'Фиолетовый'
    ent.insert(0, "#7d00ff")


if __name__ == '__main__':
    root = Tk()

    lab = Label(font="Arial 12", width=30)
    lab.pack()

    ent = Entry(width=30)
    ent.pack()

    but1 = Button(bg='#ff0000', width=20,)
    but1.bind('<Button-1>', red)
    but1.pack()

    but2 = Button(bg='#ff7d00', width=20)
    but2.bind('<Button-1>', orange)
    but2.pack()

    but3 = Button(bg='#ffff00', width=20,)
    but3.bind('<Button-1>', yellow)
    but3.pack()

    but4 = Button(bg='#00ff00', width=20,)
    but4.bind('<Button-1>', green)
    but4.pack()

    but5 = Button(bg='#007dff', width=20,)
    but5.bind('<Button-1>', cyan)
    but5.pack()

    but6 = Button(bg='#0000ff', width=20,)
    but6.bind('<Button-1>', blue)
    but6.pack()

    but7 = Button(bg='#7d00ff', width=20,)
    but7.bind('<Button-1>', violet)
    but7.pack()

    root.mainloop()
