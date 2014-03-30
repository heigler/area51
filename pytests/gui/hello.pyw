#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk


class Window(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        hello_label = ttk.Label(self, text='Hello Tkinter!')
        qui_button = ttk.Button(self, text='Quit', command=self.quit)
        hello_label.pack()
        qui_button.pack()
        self.pack()


if __name__ == '__main__':
    window = Window()
    window.master.title('Hello')
    window.master.mainloop()
