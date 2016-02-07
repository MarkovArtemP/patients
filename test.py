import sys
from PyQt4 import QtGui,QtCore
class LayoutTest(QtGui.QWidget):
    def __init__(self):
        super(LayoutTest, self).__init__()
        self.horizontalLayout = QtGui.QVBoxLayout(self)
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QtGui.QGridLayout()
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.add_button = QtGui.QPushButton("Add Items")
        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.add_button)
        self.connect(self.add_button, QtCore.SIGNAL("clicked()"), self.addButtons)
        self.setGeometry(300, 200, 400, 300)

    def addButtons(self):
        for i in range(0, 50):
            self.r_button = QtGui.QPushButton("Button %s " % i)
            self.gridLayout.addWidget(self.r_button)

app = QtGui.QApplication(sys.argv)
ex = LayoutTest()
ex.show()
sys.exit(app.exec_())

