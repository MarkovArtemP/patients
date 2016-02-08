from PyQt4.QtGui import *

from mainWindow import PatientsWindow

app = QApplication([])
win = PatientsWindow.PatientsWindow()
win.show()
app.exec_()
