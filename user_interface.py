# coding: utf-8

import tkinter as tk

"""
    Графический интерфейс голосового ассистента, 
    состоящий из одного окна с символом. 
    Символ может менять цвет, сигнализирую о состоянии ассистента.
"""


class UserInterface:
    """ Класс графического интерфейса голосового ассистента.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="☆", font=('Arial', 120, 'bold'))
        self.label.pack()

    def run(self) -> None:
        """ Запустить главный цикл. """
        self.root.mainloop()

    def mark_active(self) -> None:
        """ Сделать символ звездочки красным. """
        self.label.config(fg="red")

    def mark_passive(self):
        """ Сделать символ звездочки черным. """
        self.label.config(fg="black")
