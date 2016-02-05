import sys
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import PatientsWindow

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

def getDataList(query):
    list = []
    index = 0
    while query.next():
        row = []
        row.append(query.value(0) + ' ' + query.value(1) + ' ' + query.value(2))
        row.append(query.value(3))
        sex = "муж" if query.value(4) == 1 else "жен"
        row.append(sex)
        for i in range(3, query.record().count() - 2):
            row.append(query.value(i + 2))
        index += 1
        list.append(tuple(row))
    return list

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


app = QApplication([])

record = q.record()
labels = ['ФИО']
for i in range(3, record.count()):
    labels.append(record.fieldName(i))
index = 0

win =PatientsWindow.PatientsWindow(getDataList(q), labels)
win.show()
app.exec_()