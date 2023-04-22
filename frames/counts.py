# -*- coding: utf-8 -*-
""" This is the export_rejections module of Biovarase."""
import tkinter as tk
from tkinter import messagebox
from calendarium import Calendarium




class UI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(name='counts')

        self.parent = parent
        self.attributes('-topmost', True)
        self.resizable(0, 0)
        self.init_ui()
        self.nametowidget(".").engine.center_me(self)

    def init_ui(self):

        w = self.nametowidget(".").engine.get_init_ui(self)

        self.export_date = Calendarium(self, "Export From")
        self.export_date.get_calendarium(w, 0, 0)

        self.nametowidget(".").engine.get_export_cancel(self, self)

    def on_open(self):

        self.export_date.set_today()

        self.title("Export Counts")

    def on_export(self, evt=None):

        if self.export_date.get_date(self) == False: return
        if messagebox.askyesno(self.nametowidget(".").title(), "Export data?", parent=self) == True:
            args = (self.export_date.get_date(self),)
            self.nametowidget(".").engine.get_counts(args)
            self.on_cancel()

    def on_cancel(self, evt=None):
        self.destroy()
