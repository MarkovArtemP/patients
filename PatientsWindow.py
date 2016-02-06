import operator

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class PatientsWindow(QWidget):
    def __init__(self, data_list, header, *args):
        QWidget.__init__(self, *args)
        self.showMaximized()
        self.setWindowTitle("Patients")

        #CREATE MENU

        #create exit option
        exit = QAction('Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, SIGNAL('triggered()'), SLOT('close()'))

        #create font dialog option
        font = QAction('Font', self)
        font.setStatusTip('Change font')
        self.connect(font, SIGNAL('triggered()'), self.showFontDialog)

        #create menu bar
        menubar = QMenuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        settings = menubar.addMenu('&Settings')
        settings.addAction(font)

        #CREATE SEARCH AREA

        labels = header.copy()
        labels.__delitem__(0)
        labels.insert(0, 'Отчество')
        labels.insert(0, 'Имя')
        labels.insert(0, 'Фамилия')

        qLabels = []
        for i in labels:
            qLabels.append(QLabel(i))

        linesEdit = []
        for i in range(0, len(labels)):
            linesEdit.append(QLineEdit())

        searchHBox = QHBoxLayout()
        for i in range(0, len(labels)):
            searchHBox.addWidget(qLabels[i])
            searchHBox.addWidget(linesEdit[i])

        searchButton = QPushButton("Search")
        clearButton = QPushButton("Clear")
        buttonsHBox = QHBoxLayout()
        buttonsHBox.addWidget(searchButton)
        buttonsHBox.addWidget(clearButton)

        #CREATE TABLE

        table_model = PatientsTableModel(self, data_list, header)
        table_view = QTableView()
        table_view.setModel(table_model)
        font = QFont("Courier New", 10)
        table_view.setFont(font)
        table_view.resizeColumnsToContents()
        table_view.setSortingEnabled(True)
        self.table = table_view

        #CREATE MAIN LAYOUT
        
        vbox = QVBoxLayout()
        vbox.addWidget(menubar)
        vbox.addLayout(searchHBox)
        vbox.addLayout(buttonsHBox)
        vbox.addWidget(table_view)

        self.setLayout(vbox)
    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.table.setFont(font)
            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()


class PatientsTableModel(QAbstractTableModel):
    def __init__(self, parent, data_list, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.data_list = data_list
        self.header = header

    def rowCount(self, parent):
        return len(self.data_list)

    def columnCount(self, parent):
        return len(self.data_list[0])

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
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.data_list = sorted(self.data_list,
                                key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.data_list.reverse()
        self.emit(SIGNAL("layoutChanged()"))