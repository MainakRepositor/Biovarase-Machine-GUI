# -*- coding: utf-8 -*-
""" This is the zscore module of Biovarase."""
import tkinter as tk



class UI(tk.Toplevel):
    def __init__(self, parent, index=None):
        super().__init__(name="zscore")

        self.parent = parent
        self.attributes("-topmost", True)
        self.transient(parent)
        self.resizable(0, 0)
        self.nametowidget(".").engine.center_me(self)
        self.init_ui()


    def init_ui(self):

        w = self.nametowidget(".").engine.get_init_ui(self)

        items = ("Z-Score", "2.33", "2.05", "0.75", "1.88", "1.75", "1.65")

        r = 0
        c = 0
        for i in items:
            tk.Label(w, text=i).grid(row=r, column=c, sticky=tk.W, padx=10, pady=10)
            r += 1

        items = ("Probability", "p>0.01", "p>0.02", "p>0.03", "p>0.04", "p>0.05")

        r = 0
        c = 1
        for i in items:
            tk.Label(w, text=i).grid(row=r, column=c, sticky=tk.W, padx=10, pady=10)
            r += 1

        items = ("Probability","99%", "98%", "97%", "96%", "95%")
        r = 0
        c = 2
        for i in items:
            tk.Label(w, text=i).grid(row=r, column=c, sticky=tk.W, padx=10, pady=10)
            r += 1


    def on_open(self,):

        self.title("Probability")


    def on_cancel(self, evt=None):
        self.destroy()
