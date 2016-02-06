import operator

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class PatientsWindow(QWidget):
    def __init__(self, data_list, header, *args):
        QWidget.__init__(self, *args)
        self.showMaximized()
        self.setWindowTitle("Patients")

        # CREATE MENU

        # create exit option
        exit = QAction('Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, SIGNAL('triggered()'), SLOT('close()'))

        # create font dialog option
        font = QAction('Font', self)
        font.setStatusTip('Change font')
        self.connect(font, SIGNAL('triggered()'), self.showFontDialog)

        # create menu bar
        menubar = QMenuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        settings = menubar.addMenu('&Settings')
        settings.addAction(font)

        # CREATE SEARCH AREA

        searchVBox = QVBoxLayout()

        # create top buttons

        addButton = QPushButton("Add search field")
        self.connect(self.addButton, SIGNAL('clicked()'), self.add)
        removeAllButton = QPushButton("Remove all")
        topButtonsHBox = QHBoxLayout()
        topButtonsHBox.addWidget(addButton)
        topButtonsHBox.addWidget(removeAllButton)
        searchVBox.addLayout(topButtonsHBox)

        # create search fields
        labels = header.copy()
        labels.__delitem__(0)
        labels.insert(0, 'Отчество')
        labels.insert(0, 'Имя')
        labels.insert(0, 'Фамилия')

        fieldsHBox = QHBoxLayout()
        sField = SearchField(labels, fieldsHBox)
        fieldsHBox.addLayout(sField)
        searchVBox.addLayout(fieldsHBox)

        # Create bottom buttons
        searchButton = QPushButton("Search")
        clearButton = QPushButton("Clear all")
        botButtonsHBox = QHBoxLayout()
        botButtonsHBox.addWidget(searchButton)
        botButtonsHBox.addWidget(clearButton)
        searchVBox.addLayout(botButtonsHBox)

        # CREATE TABLE

        table_model = PatientsTableModel(self, data_list, header)
        table_view = QTableView()
        table_view.setModel(table_model)
        font = QFont("Courier New", 10)
        table_view.setFont(font)
        table_view.resizeColumnsToContents()
        table_view.setSortingEnabled(True)
        self.table = table_view

        # CREATE MAIN LAYOUT

        vbox = QVBoxLayout()
        vbox.addWidget(menubar)
        vbox.addLayout(searchVBox)
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
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.data_list = sorted(self.data_list,
                                key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.data_list.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class SearchField(QHBoxLayout):
    def __init__(self, cbItems, parent):
        QHBoxLayout.__init__(self)
        self.parent = parent
        self.cb = QComboBox()
        for i in cbItems:
            self.cb.addItem(i)
        self.addWidget(self.cb)

        self.lineEdit = QLineEdit()
        self.addWidget(self.lineEdit)

        self.removeButton = QPushButton("Remove")
        self.connect(self.removeButton, SIGNAL('clicked()'), self.delete)
        self.addWidget(self.removeButton)

    def delete(self):
        self.cb.close()
        self.lineEdit.close()
        self.removeButton.close()
        self.parent.removeItem(self)
