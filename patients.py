import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

app = QApplication(sys.argv)
table = QTableWidget()
table.setWindowTitle("Patients")

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("127.0.0.1")
db.setPort(3306)
db.setDatabaseName("patients")
db.setUserName("root")
db.setPassword("bd2crcv6")
ok = db.open()

query = QSqlQuery(db)
query.exec_(
        "SELECT Client.lastName, Client.firstName, Client.patrName, DATE_FORMAT(Client.birthDate, '%d.%m.%Y'), Client.sex, " +
        "rbDocumentType.name, ClientDocument.serial, ClientDocument.number, DATE_FORMAT(ClientDocument.date, '%d.%m.%Y'), " +
        "rbPolicyType.name, ClientPolicy.serial, ClientPolicy.number, DATE_FORMAT(ClientPolicy.begDate, '%d.%m.%Y'), DATE_FORMAT(ClientPolicy.endDate, '%d.%m.%Y'), ClientPolicy.name, ClientPolicy.note " +
        "FROM Client " +
        "LEFT JOIN ClientDocument ON ClientDocument.client_id = Client.id " +
        "LEFT JOIN ClientPolicy ON ClientPolicy.client_id = Client.id " +
        "LEFT JOIN rbDocumentType ON rbDocumentType.id = ClientDocument.documentType_id " +
        "LEFT JOIN rbPolicyType ON rbPolicyType.id = ClientPolicy.policyType_id " +
        ";")

table.setColumnCount(query.record().count() - 2)
table.setRowCount(query.size())

index = 0
while query.next():
    table.setItem(index, 0, QTableWidgetItem(query.value(0) + ' ' + query.value(1) + ' ' + query.value(2)))
    table.setItem(index, 1, QTableWidgetItem(query.value(3)))
    sex = "муж" if query.value(4) == 1 else "жен"
    table.setItem(index, 2, QTableWidgetItem(sex))
    for i in range(3, query.record().count() - 2):
        table.setItem(index, i, QTableWidgetItem(query.value(i + 2)))
    index += 1

table.show()

sys.exit(app.exec_())
