from PyQt4.QtGui import *

from searchArea.Field import Field


class FieldsWidget(QWidget):
    def __init__(self, labels):
        QWidget.__init__(self)
        self.setFixedHeight(200)
        self.labels = labels

        # Container Widget
        widget = QWidget()
        # Layout of Container Widget
        self.content = QVBoxLayout(self)

        widget.setLayout(self.content)

        # Scroll Area Properties
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        # Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

    def addContent(self):
        field = Field(self.labels, self.content)
        self.content.addLayout(field)

    def removeAll(self):
        count = self.content.count()
        for i in range(count - 1, -1, -1):
            self.content.itemAt(i).delete()

    def clearAll(self):
        for i in range(self.content.count()):
            self.content.itemAt(i).lineEdit.setText(None)

    def collectQueryParameters(self):
        parameters = []
        for i in range(self.content.count()):
            parameters.append(self.content.itemAt(i).getParameters())
        return parameters

