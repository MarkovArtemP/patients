from PyQt4.QtCore import *
from PyQt4.QtGui import *

from databaseQuery.Query import Query


class Field(QHBoxLayout):
    def __init__(self, parent):
        QHBoxLayout.__init__(self)
        self.parent = parent
        query = Query()
        fieldsItems = query.getHeader()
        self.fields = QComboBox()
        for i in fieldsItems:
            self.fields.addItem(i)
        self.addWidget(self.fields)

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
        self.fields.close()
        self.cb2.close()
        self.lineEdit.close()
        self.removeButton.close()
        self.parent.removeItem(self)

    def getParameters(self):
        parameters = []
        parameters.append(self.fields.currentText())
        parameters.append(self.cb2.currentText())
        parameters.append(self.lineEdit.text().split("'")[0])
        return parameters

