from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *

from databaseQuery.Query import Query


class DatabaseSettings(QDialog):
    def __init__(self, parent, start=False):
        self.start = start
        self.parent =parent
        QDialog.__init__(self)
        self.setWindowTitle("Database settings")

        grid = QGridLayout()

        hostLabel = QLabel('Host')
        self.hostLine = QLineEdit()
        self.hostLine.setText('127.0.0.1')
        grid.addWidget(hostLabel, 1, 0)
        grid.addWidget(self.hostLine, 1, 1)

        portLabel = QLabel('Port')
        self.portLine = QLineEdit()
        self.portLine.setText('3306')
        grid.addWidget(portLabel, 2, 0)
        grid.addWidget(self.portLine, 2, 1)

        databaseLabel = QLabel('Database')
        self.databaseLine = QLineEdit()
        self.databaseLine.setText('patients')
        grid.addWidget(databaseLabel, 3, 0)
        grid.addWidget(self.databaseLine, 3, 1)

        userLabel = QLabel('Username')
        self.userLine = QLineEdit()
        self.userLine.setText('root')
        grid.addWidget(userLabel, 4, 0)
        grid.addWidget(self.userLine, 4, 1)

        passwordLabel = QLabel('Password')
        self.passwordLine = QLineEdit()
        self.passwordLine.setEchoMode(QLineEdit.Password)
        grid.addWidget(passwordLabel, 5, 0)
        grid.addWidget(self.passwordLine, 5, 1)

        okButton = QPushButton("ok")
        self.connect(okButton, SIGNAL('clicked()'), self.setParameters)
        cancelButton = QPushButton("Cancel")
        self.connect(cancelButton, SIGNAL('clicked()'), self.close)
        grid.addWidget(okButton, 6, 0)
        grid.addWidget(cancelButton, 6, 1)

        self.setLayout(grid)

        self.exec_()

    def setParameters(self):
        parameters = {}
        parameters['host'] = self.hostLine.text()
        parameters['port'] = self.portLine.text()
        parameters['database'] = self.databaseLine.text()
        parameters['username'] = self.userLine.text()
        parameters['password'] = self.passwordLine.text()
        if self.start:
            Query(parameters)
        else:
            query = Query()
            query.refreshParameters(parameters)
            self.parent.table.refreshTable()
        self.close()
