# -*- coding: utf-8 -*-
""" This is the export_rejections module of Biovarase."""
import tkinter as tk
from tkinter import messagebox
from calendarium import Calendarium




class UI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(name='export_rejection')

        self.parent = parent
        self.resizable(0, 0)
        self.transient(parent)

        self.init_ui()
        self.nametowidget(".").engine.center_me(self)

    def init_ui(self):

        w = self.nametowidget(".").engine.get_init_ui(self)

        r = 0
        self.start_date = Calendarium(self, "Start Date")
        self.start_date.get_calendarium(w, r)

        self.nametowidget(".").engine.get_export_cancel(self, w)

    def on_open(self):

        self.start_date.set_today()

        self.title("Export Rejections Data")

    def on_export(self, evt=None):

        if self.start_date.get_date(self) == False: return

        if messagebox.askyesno(self.nametowidget(".").title(), "Export data?", parent=self) == True:
            args = (self.start_date.get_date(self),)
            self.nametowidget(".").engine.get_rejections(args)
            self.on_cancel()

    def on_cancel(self, evt=None):
        self.destroy()
