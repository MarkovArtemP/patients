from PyQt4.QtGui import *
from PyQt4.QtCore import *
from searchArea.Field import Field


class SearchArea(QVBoxLayout):
    def __init__(self, labels):
        self.labels = labels
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
        sField = Field(self.labels, self.fieldsVBox)
        self.fieldsVBox.addLayout(sField)

    def removeAll(self):
        self.fieldsVBox.count()
        count = self.fieldsVBox.count()
        for i in range(count - 1, -1, -1):
            self.fieldsVBox.itemAt(i).delete()

    def clearAll(self):
        self.fieldsVBox.count()
        count = self.fieldsVBox.count()
        for i in range(count - 1, -1, -1):
            self.fieldsVBox.itemAt(i).lineEdit.setText(None)
