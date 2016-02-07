from PyQt4.QtGui import *
from PyQt4.QtCore import *
from searchArea.Fields import FieldsWidget


class SearchArea(QVBoxLayout):
    def __init__(self, labels):
        QVBoxLayout.__init__(self)
        self.fieldsWidget = FieldsWidget(labels)

        # Create top buttons
        addButton = QPushButton("Add search field")
        self.connect(addButton, SIGNAL('clicked()'), self.fieldsWidget.addContent)
        removeAllButton = QPushButton("Remove all fields")
        self.connect(removeAllButton, SIGNAL('clicked()'), self.fieldsWidget.removeAll)
        topButtonsHBox = QHBoxLayout()
        topButtonsHBox.addWidget(addButton)
        topButtonsHBox.addWidget(removeAllButton)
        self.addLayout(topButtonsHBox)

        # Create search fields layout

        self.fieldsVBox = QVBoxLayout()
        self.fieldsVBox.addWidget(self.fieldsWidget)
        self.addLayout(self.fieldsVBox)

        # Create bottom buttons
        botButtonsHBox = QHBoxLayout()

        self.clearButton = QPushButton("Clear all fields")
        self.connect(self.clearButton, SIGNAL('clicked()'), self.fieldsWidget.clearAll)
        botButtonsHBox.addWidget(self.clearButton)

        self.searchButton = QPushButton("Search")
        self.connect(self.searchButton, SIGNAL('clicked()'), self.search)
        botButtonsHBox.addWidget(self.searchButton)

        self.addLayout(botButtonsHBox)

    def search(self):
        print(self.fieldsWidget.collectQueryParameters())


