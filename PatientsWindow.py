from PyQt4.QtCore import SLOT
from PyQt4.QtGui import *

from menu.MenuBar import MenuBar
from searchArea.AreaLayout import SearchArea
from patientsTable.View import PatientsTableView


class PatientsWindow(QWidget):
    def __init__(self, data_list, header, *args):
        QWidget.__init__(self, *args)
        self.showMaximized()
        self.setWindowTitle("Patients")

        # CREATE MENU

        menubar = MenuBar(self)

        # CREATE SEARCH AREA

        self.labels = header.copy()
        self.labels.__delitem__(0)
        self.labels.insert(0, 'Отчество')
        self.labels.insert(0, 'Имя')
        self.labels.insert(0, 'Фамилия')
        searchArea = SearchArea(self.labels)

        # CREATE TABLE

        table_view = PatientsTableView(data_list, header)

        # CREATE MAIN LAYOUT

        vbox = QVBoxLayout()
        vbox.addWidget(menubar)
        vbox.addLayout(searchArea)
        vbox.addWidget(table_view)

        self.setLayout(vbox)
