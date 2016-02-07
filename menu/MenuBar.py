from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MenuBar(QMenuBar):
    def __init__(self, parent):
        QMenuBar.__init__(self)

        # create exit option
        exit = QAction('Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, SIGNAL('triggered()'), parent.close)

        # create font dialog option
        font = QAction('Font', self)
        font.setStatusTip('Change font')
        self.connect(font, SIGNAL('triggered()'), self.showFontDialog)

        # create menu bar
        file = self.addMenu('&File')
        file.addAction(exit)
        settings = self.addMenu('&Settings')
        settings.addAction(font)

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.table.setFont(font)
            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()
