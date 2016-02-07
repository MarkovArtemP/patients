from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Field(QHBoxLayout):
    def __init__(self, cbItems, parent):
        QHBoxLayout.__init__(self)
        self.parent = parent
        self.cb1 = QComboBox()
        for i in cbItems:
            self.cb1.addItem(i)
        self.addWidget(self.cb1)

        self.cb2 = QComboBox()
        self.cb2.addItem("contains")
        self.cb2.addItem("not contains")
        self.cb2.addItem("is")
        self.cb2.addItem("is not")
        self.addWidget(self.cb2)

        self.lineEdit = QLineEdit()
        self.addWidget(self.lineEdit)

        self.removeButton = QPushButton("Remove")
        self.connect(self.removeButton, SIGNAL('clicked()'), self.delete)
        self.addWidget(self.removeButton)

    def delete(self):
        self.cb1.close()
        self.cb2.close()
        self.lineEdit.close()
        self.removeButton.close()
        self.parent.removeItem(self)

    def getParameters(self):
        parameters = []
        parameters.append(self.cb1.currentText())
        parameters.append(self.cb2.currentText())
        parameters.append(self.lineEdit.text())
        return parameters

