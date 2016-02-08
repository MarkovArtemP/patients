from PyQt4.QtGui import *
from PyQt4.QtCore import *

from menu.DatabaseSettings import DatabaseSettings


class MenuBar(QMenuBar):
    def __init__(self, parent):
        QMenuBar.__init__(self)
        self.parent = parent
        # create exit option
        exit = QAction('Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, SIGNAL('triggered()'), parent.close)

        # create font dialog option
        font = QAction('Font', self)
        font.setStatusTip('Change font')
        self.connect(font, SIGNAL('triggered()'), self.showFontDialog)

        # create database settings dialog option
        database = QAction('Database', self)
        database.setStatusTip('Change database settings')
        self.connect(database, SIGNAL('triggered()'), lambda: DatabaseSettings(self.parent))

        # create menu bar
        file = self.addMenu('&File')
        file.addAction(exit)
        settings = self.addMenu('&Settings')
        settings.addAction(font)
        settings.addAction(database)

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.parent.table.setFont(font)
            self.parent.table.resizeColumnsToContents()
            self.parent.table.resizeRowsToContents()
