# -*- coding: utf-8 -*-


from tkinter import Scrollbar, TclError


class AutoScrollbar(Scrollbar):

    """Eine Bildlaufleiste, die ausgeblendet wird, wenn sie nicht benötigt wird.
    Es funktioniert nur, wenn eine Gittergeometrie verwendet wird.
    Quelle : http://effbot.org/zone/tkinter-autoscrollbar.htm
    """

    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove ist derzeit nicht in Tkinter enthalten.
            # Die Methode tk.call wird in der Tat auf der
            # scrollbar
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise (TclError, "Sie können mit diesem Widget keine Packs verwenden")

    def place(self, **kw):
        raise (TclError, "Mit diesem Widget können Sie keinen Platz verwenden")
