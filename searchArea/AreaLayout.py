from PyQt4.QtGui import *
from PyQt4.QtCore import *
from searchArea.Fields import FieldsWidget


class SearchArea(QVBoxLayout):
    def __init__(self, labels):
        QVBoxLayout.__init__(self)

        # Create top buttons
        addButton = QPushButton("Add search field")
        self.connect(addButton, SIGNAL('clicked()'), self.addField)
        removeAllButton = QPushButton("Remove all fields")
        self.connect(removeAllButton, SIGNAL('clicked()'), self.removeAll)
        topButtonsHBox = QHBoxLayout()
        topButtonsHBox.addWidget(addButton)
        topButtonsHBox.addWidget(removeAllButton)
        self.addLayout(topButtonsHBox)

        # Create search fields layout

        self.fieldsVBox = QVBoxLayout()
        self.fieldsWidget = FieldsWidget(labels)
        self.fieldsVBox.addWidget(self.fieldsWidget)
        self.addLayout(self.fieldsVBox)

        # Create bottom buttons
        botButtonsHBox = QHBoxLayout()

        self.clearButton = QPushButton("Clear all fields")
        self.connect(self.clearButton, SIGNAL('clicked()'), self.clearAll)
        botButtonsHBox.addWidget(self.clearButton)

        searchButton = QPushButton("Search")
        botButtonsHBox.addWidget(searchButton)

        self.addLayout(botButtonsHBox)

    def addField(self):
        self.fieldsWidget.addContent()

    def removeAll(self):
        self.fieldsWidget.removeAll()

    def clearAll(self):
        self.fieldsWidget.clearAll()
