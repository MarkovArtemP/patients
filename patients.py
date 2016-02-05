import sys
from PyQt4.QtGui import *
from PyQt4.QtSql import *

def getQuery(host, port, database, user, password):
    db = QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName(host)
    db.setPort(port)
    db.setDatabaseName(database)
    db.setUserName(user)
    db.setPassword(password)
    if db.open():
        return QSqlQuery(db)
    else:
        return None

def getTable(query):
    table = QTableWidget()
    table.setWindowTitle("Patients")
    table.setRowCount(query.size())
    table.setColumnCount(query.record().count() - 2)
    record = q.record()
    labels = ['ФИО']
    for i in range(3, record.count()):
        labels.append(record.fieldName(i))
    table.setHorizontalHeaderLabels(labels)
    index = 0
    while query.next():
        table.setItem(index, 0, QTableWidgetItem(query.value(0) + ' ' + query.value(1) + ' ' + query.value(2)))
        table.setItem(index, 1, QTableWidgetItem(query.value(3)))
        sex = "муж" if query.value(4) == 1 else "жен"
        table.setItem(index, 2, QTableWidgetItem(sex))
        for i in range(3, query.record().count() - 2):
            table.setItem(index, i, QTableWidgetItem(query.value(i + 2)))
        index += 1
    table.resizeColumnsToContents()
    return table

# TODO init params
h = "127.0.0.1"
p = 3306
dbase = "patients"
u = "root"
passwd = "bd2crcv6"
q = getQuery(h, p, dbase, u, passwd)
q.exec_(
        "SELECT Client.lastName, Client.firstName, Client.patrName, " +
        "DATE_FORMAT(Client.birthDate, '%d.%m.%Y') AS 'Дата рождения', " +
        "Client.sex AS 'Пол', " +
        "rbDocumentType.name AS 'Тип документа', " +
        "ClientDocument.serial AS 'Серия', " +
        "ClientDocument.number AS 'Номер', " +
        "DATE_FORMAT(ClientDocument.date, '%d.%m.%Y') AS 'Дата выдачи', " +
        "rbPolicyType.name AS 'Тип полиса', " +
        "ClientPolicy.serial AS 'Серия', " +
        "ClientPolicy.number AS 'Номер', " +
        "DATE_FORMAT(ClientPolicy.begDate, '%d.%m.%Y') AS 'Дата начала', " +
        "DATE_FORMAT(ClientPolicy.endDate, '%d.%m.%Y') AS 'Дата окончания', " +
        "ClientPolicy.name AS 'Name', " +
        "ClientPolicy.note AS 'Note' " +
        "FROM Client " +
        "LEFT JOIN ClientDocument ON ClientDocument.client_id = Client.id " +
        "LEFT JOIN ClientPolicy ON ClientPolicy.client_id = Client.id " +
        "LEFT JOIN rbDocumentType ON rbDocumentType.id = ClientDocument.documentType_id " +
        "LEFT JOIN rbPolicyType ON rbPolicyType.id = ClientPolicy.policyType_id " +
        ";")

app = QApplication(sys.argv)
tabl = getTable(q)
tabl.show()
sys.exit(app.exec_())