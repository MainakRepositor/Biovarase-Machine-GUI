# -*- coding: utf-8 -*-
""" This is the analytical module of Biovarase.
It shows analyticak goals rules"""
import tkinter as tk



class UI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(name="analitical")

        self.parent = parent
        self.attributes("-topmost", True)
        self.resizable(0, 0)
        self.init_ui()
        self.nametowidget(".").engine.center_me(self)

    def init_ui(self):

        w = self.nametowidget(".").engine.get_init_ui(self)

        items = (("k CV:", None), ("0.25", "green"), ("0.50", "yellow"), ("0.75", "red"),)

        r = 0
        c = 0
        for i in items:
            tk.Label(w, bg=i[1], text=i[0]).grid(row=r, column=c, sticky=tk.W, padx=10, pady=10)
            r += 1


        items = (("k Bias:", None), ("0.125<= k <= 0.25", "green"),
                 ("0.25<= k <= 0.375", "yellow"), ("k > 0.375", "red"),)

        r = 0
        c = 1
        for i in items:
            tk.Label(w, bg=i[1], text=i[0]).grid(row=r, column=c, sticky=tk.W, padx=10, pady=10)
            r += 1

        items = (("Eta:", None),
                 ("ETa < 1.65 (0.25 CVi) + 0.125 (CVi2+ CVg2) ½ ", "green"),
                 ("ETa < 1.65 (0.50 CVi) + 0.25 (CVi2 + CVg2) ½", "yellow"), ("ETa < 1.65 (0.75 CVi) + 0.375 (CVi2+ CVg2) ½", "red"),)

        r = 0
        c = 2
        for i in items:
            tk.Label(w, bg=i[1], text=i[0]).grid(row=r, column=c, sticky=tk.W, padx=10, pady=10)
            r += 1


    def on_open(self,):

        self.title("Analytical Goals Explained")


    def on_cancel(self, evt=None):
        self.destroy()
