# -*- coding: utf-8 -*-


from tkinter import (
    LabelFrame,
    Scrollbar,
    Menu,
    Text,
    RIDGE,
    W,
    E,
    N,
    S,
    WORD,
    INSERT,
    END,
    HORIZONTAL,
)
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askquestion, showinfo, YES, WARNING


class Editor(object):

    """
    Fenster für den Assembly-Editor
    """

    def __init__(self, master, calcolatore):
        """
        Initialisiert Editor-Fensterrahmen
        """
        self.master = master
        self.CD = calcolatore
        # Codice Assembly
        self.codice = LabelFrame(
            self.master,
            text="Assembly-Code",
            relief=RIDGE,
            borderwidth=5,
            labelanchor="n",
            pady=5,
        )
        self.codice.rowconfigure(0, weight=1)
        self.codice.columnconfigure(0, weight=1)
        self.codice.grid(row=1, column=0, rowspan=3, columnspan=5, sticky=W + E + N + S)

        self.menubar = Menu(self.master)
        self.create_widgets(self.menubar)

    def create_widgets(self, menubar):
        """
        Programmlayout erstellen, Editorfenster
        """
        # Menu
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu.add_command(label="Öffnen", command=self.openFile)
        self.filemenu.add_command(label="Speichern", command=self.saveFile)
        self.filemenu.add_command(label="Abbrechen", command=self.deleteFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Beenden", command=self.exit)
        menubar.add_cascade(label="Optionen", menu=self.filemenu)
        self.master.config(menu=self.menubar)

        self.helpmenu = Menu(menubar, tearoff=0)
        self.helpmenu.add_command(label="Informationen", command=self.infor)
        self.helpmenu.add_command(label="Legende", command=self.leg)
        self.helpmenu.add_command(label="Leitfaden", command=self.guide)
        menubar.add_cascade(label="Hilfe", menu=self.helpmenu)

        # Codice Assembly
        self.insertAssembly = Text(self.codice, width=50, height=30, wrap=WORD)
        self.insertAssemblyScrollbar = Scrollbar(self.codice)
        self.insertAssemblyScrollbar.config(command=self.insertAssembly.yview)
        self.insertAssembly.config(yscrollcommand=self.insertAssemblyScrollbar.set)
        self.insertAssemblyScrollbar.grid(row=0, column=1, sticky=N + S)
        self.insertAssembly.grid(row=0, column=0, sticky=W)

    def exit(self):
        """
        Programm beenden
        """
        if askquestion("Beenden?", "Möchten Sie das Programm wirklich beenden?") == YES:
            self.master.quit()
            self.master.destroy()
        else:
            showinfo(
                "Tipp", """Vielleicht ist es besser, eine Pause zu machen!""", icon=WARNING
            )

    def openFile(self):
        """
        Assembly-Datei zur Bearbeitung öffnen
        """
        path = askopenfilename(
            title="Assembly-Datei öffnen",
            filetypes=[("Assembly-Dateien", ".asm"), ("Textdateien", ".txt"), ("Alle Dateien", "*")],
        )
        if path != "":
            with open(path, "r") as cur_file:
                self.insertAssembly.delete(1.0, END)
                self.insertAssembly.insert(INSERT, cur_file.read())

    def deleteFile(self):
        """
        Aktuelles Programm löschen
        """
        if (
            askquestion("Löschen?", "Möchten Sie das aktuelle Programm unwiederbringlich löschen?")
            == YES
        ):
            self.insertAssembly.delete(1.0, END)

    def saveFile(self):
        """
        Aktuelles Programm speichern
        """
        programContent = self.insertAssembly.get(1.0, END)
        programContent = programContent.encode("ascii", "ignore")
        path = asksaveasfilename(
            title="Speichern unter...",
            defaultextension=[("Assembly-Datei", ".asm"), ("Textdatei", ".txt"), ("Alle Dateien", "*")],
            filetypes=[("Assembly-Datei", ".asm"), ("Textdatei", ".txt"), ("Alle Dateien", "*")],
        )

        if path != "":
            file = open(path, "w")
            file.write(str(programContent))
            file.close()

    @staticmethod
    def infor():
        """
        Lizenzinfos anzeigen
        """
        infoName = """PDP-8 Emulator"""
        infoString = """
    PDP-8 Emulator
    
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    Version = 1.6.2
    
    Tested with = python 2.6 & 2.7
    -------------------------------------------------------------------
        
    The MIT License (MIT)

    Copyright (c) 2015 Mirco

    Permission is hereby granted, free of charge, to any person 
    obtaining a copy of this software and associated documentation 
    files (the "Software"), to deal in the Software without 
    restriction, including without limitation the rights to use, 
    copy, modify, merge, publish, distribute, sublicense, and/or 
    sell copies of the Software, and to permit persons to whom the 
    Software is furnished to do so, subject to the following 
    conditions:

    The above copyright notice and this permission notice shall 
    be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY 
    KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
    PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
    OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
    OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    
    -------------------------------------------------------------------
        
    Contact: m.tracolli@gmail.com

    Collaborators : Walter Valentini
    """
        showinfo(infoName, infoString)

    @staticmethod
    def leg():
        """
        Informationen in Farbe
        """
        infoName = """Über PDP-8"""
        infoString = """
        Rosso = indirizzo puntato da PC
        Giallo = indirizzo puntato da MAR
        Verde = ultima istruzione eseguita
        """
        showinfo(infoName, infoString)

    @staticmethod
    def guide():
        """
        Kleiner Leitfaden
        """
        infoName = """PDP-8 Leitfaden"""
        infoString = """
    LOAD = Assemply Programm in den Computer laden.
    
    STEP = Weiterschalten um die angegebene Anzahl von Schritten (Standardmäßig 1).
            Ein Schritt ist gleichbedeutend mit der Ausführung einer einzigen Anweisung.
    
    mini STEP = Führt einen einzelnen Zyklus auf Grundlage der
            F- und R-Variablen des Computers aus.
            
    micro STEP = Führt eine Mikroinstruktion aus.
            
    Set n STEP = Schrittzahl einstellen.
        
    Set Delay = Ausführungsverzögerung einstellen.
        
    START = Das System startet, aber nicht die Ausführung des Codes. Um
            den Code auszuführen, STEP verwenden oder einmal ausführen
            sobald die Maschine gestartet ist.
            
    RESET = Setzt das System in den Ausgangszustand zurück.
        
    STOP = Stoppt System & ausführung des aktuellen Programms.
    
    BREAK = Aggiunge o toglie un break alla cella indicata
            in esadecimale.
    
    CONTINUA = Continua l'esecuzione del programma dopo un break.
               Equivale a premere in sequenza START ed ESEGUI.
            
    ESEGUI = Esegue il codice fino all'istruzione HLT, che
            arresta la macchina.
        """
        showinfo(infoName, infoString)
