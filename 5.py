#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, в которой имеется несколько объединенных
в группу радиокнопок, индикатор которых выключен (indicatoron=0).
Если какая-нибудь кнопка включается, то в метке должна отображаться
соответствующая ей информация. Обычных кнопок в окне быть не должно.
"""

from tkinter import Tk, StringVar, Label, LEFT, Radiobutton, Frame, TOP


def get_contact():
    label.config(text=people[var.get()])


if __name__ == "__main__":
    people = {
        'Вася': '+79283457619',
        'Петя': '+79059993409',
        'Маша': '+79643482810'
    }

    root = Tk()

    f_left = Frame(root)
    f_left.pack(side=LEFT)

    label = Label(root, justify='center', width=20, text='Нажмите на имя')
    label.pack(side=LEFT, expand=True)

    var = StringVar()

    for name in people.keys():
        Radiobutton(f_left, width=15, text=name, indicatoron=0, variable=var,
                    value=name, command=get_contact).pack(side=TOP)

    root.mainloop()
