from PyQt4.QtGui import *
from PyQt4.QtCore import *
from searchArea.Field import Field

class FieldsLayout(QVBoxLayout):
    def __init__(self):
        QVBoxLayout.__init__(self)
        self.horizontalLayout = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()

        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QGridLayout()
        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.add_button = QPushButton("Add Items")

        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.add_button)
        self.connect(self.add_button, SIGNAL("clicked()"), self.addButtons)
        self.setGeometry(300, 200, 400, 300)