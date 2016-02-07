from patientsTable.Model import PatientsTableModel
from PyQt4.QtGui import *


class PatientsTableView(QTableView):
    def __init__(self, data_list, header):
        QTableView.__init__(self)
        table_model = PatientsTableModel(self, data_list, header)
        self.setModel(table_model)
        # font = QFont("Courier New", 10)
        # table_view.setFont(font)
        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
