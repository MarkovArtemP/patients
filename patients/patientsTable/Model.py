import operator

from PyQt4.QtCore import *

from databaseQuery.Query import Query


class PatientsTableModel(QAbstractTableModel):
    def __init__(self, parent, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        query = Query()

        self.header = query.getHeader()

        self.data_list = query.getDataList()

    def rowCount(self, parent):
        return len(self.data_list)

    def columnCount(self, parent):
        if len(self.data_list)>0:
            return len(self.data_list[0])
        else:
            return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.data_list[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.data_list = sorted(self.data_list,
                                key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.data_list.reverse()
        self.emit(SIGNAL("layoutChanged()"))