from PyQt4.QtGui import *

from searchArea.Field import Field


class FieldsWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedHeight(200)

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
        field = Field(self.content)
        self.content.addLayout(field)

    def removeAll(self):
        count = self.content.count()
        for i in range(count - 1, -1, -1):
            self.content.itemAt(i).delete()

    def clearAll(self):
        for i in range(self.content.count()):
            self.content.itemAt(i).lineEdit.setText(None)

    def collectQueryParameters(self):
        where = ''
        for i in range(self.content.count()):
            param = self.content.itemAt(i).getParameters()
            if param[2] == '':
                continue
            where += " " + param[0] + " "
            if param[1] == 'contains':
                where += "LIKE '%" + param[2] + "%' "
            elif param[1] == 'not contains':
                where += "NOT LIKE '%" + param[2] + "%' "
            elif param[1] == 'is':
                where += "LIKE '" + param[2] + "' "
            elif param[1] == 'is not':
                where += "NOT LIKE '" + param[2] + "' "
            if i != self.content.count() - 1:
                where += 'AND '
        if where == '':
            where = 'TRUE'
        return where
