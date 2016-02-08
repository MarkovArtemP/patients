from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *

from databaseQuery.Query import Query
from menu.MenuBar import MenuBar
from searchArea.AreaLayout import SearchArea
from patientsTable.View import PatientsTableView
from menu.DatabaseSettings import DatabaseSettings


class PatientsWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.showMaximized()
        self.setWindowTitle("Patients")

        # CREATE MENU
        menubar = MenuBar(self)

        # CREATE SEARCH AREA
        self.searchArea = SearchArea()
        self.connect(self.searchArea.searchButton, SIGNAL('clicked()'), self.doSearch)

        # CREATE TABLE
        DatabaseSettings(self, True)
        self.table = PatientsTableView()

        # CREATE MAIN LAYOUT
        vbox = QVBoxLayout()
        vbox.addWidget(menubar)
        vbox.addLayout(self.searchArea)
        vbox.addWidget(self.table)

        self.setLayout(vbox)

    def doSearch(self):
        query = Query()
        query.refreshQuery(self.searchArea.fieldsWidget.collectQueryParameters())
        self.table.refreshTable()
