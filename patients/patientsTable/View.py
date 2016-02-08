from patientsTable.Model import PatientsTableModel
from PyQt4.QtGui import *


class PatientsTableView(QTableView):
    def __init__(self):
        QTableView.__init__(self)
        self.refreshTable()

    def refreshTable(self):
        self.clearSpans()
        table_model = PatientsTableModel(self)
        self.setModel(table_model)
        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
