from PyQt4.QtGui import *


class ErrorDialog(QDialog):
    def __init__(self, type, message=''):
        QDialog.__init__(self)
        self.setWindowTitle("Error")
        grid = QGridLayout()
        self.type = QLabel(type)
        grid.addWidget(self.type)
        self.message = QLabel(message)
        grid.addWidget(self.message)
        self.setLayout(grid)
        self.exec_()
