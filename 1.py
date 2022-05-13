#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решите задачу: напишите простейший калькулятор, состоящий из двух
текстовых полей, куда пользователь вводит числа, и четырех кнопок 
"+", "-", "*", "/". Результат вычисления должен отображаться в метке.
Если арифметическое действие выполнить невозможно (например, если были
введены буквы, а не числа), то в метке должно появляться слово "ошибка"
"""

from tkinter import Tk, Entry, Button, Label


def add(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        lab['text'] = a + b
    except ValueError:
        lab['text'] = 'Ошибка'


def sub(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        lab['text'] = a - b
    except ValueError:
        lab['text'] = 'Ошибка'


def mul(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        lab['text'] = a * b
    except ValueError:
        lab['text'] = 'Ошибка'


def div(event):
    try:
        a = float(ent1.get())
        b = float(ent2.get())
        lab['text'] = a / b
    except ValueError:
        lab['text'] = 'Ошибка'
    except ZeroDivisionError:
        lab['text'] = 'Ошибка деления на 0'


if __name__ == '__main__':
    root = Tk()

    ent1 = Entry(width=30)
    ent1.pack()

    ent2 = Entry(width=30)
    ent2.pack()

    but1 = Button(text='+')
    but1.bind('<Button-1>', add)
    but1.pack()

    but2 = Button(text='-')
    but2.bind('<Button-1>', sub)
    but2.pack()

    but3 = Button(text='*')
    but3.bind('<Button-1>', mul)
    but3.pack()

    but4 = Button(text='/')
    but4.bind('<Button-1>', div)
    but4.pack()

    lab = Label(width=35)
    lab.config(bd=14)
    lab.pack()

    root.mainloop()
