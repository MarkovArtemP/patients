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
        for i in range(0, query.record().count()):
            row.append(query.value(i))
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
        "SELECT CONCAT_WS(' ', Client.lastName, Client.firstName, Client.patrName) AS ФИО, " +
        "DATE_FORMAT(Client.birthDate, '%d.%m.%Y') AS 'Дата рождения', " +
        "((YEAR(CURRENT_DATE) - YEAR(Client.birthDate)) - (DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(Client.birthDate, '%m%d'))) AS Возраст, " +
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
labels = []
for i in range(0, record.count()):
    labels.append(record.fieldName(i))
index = 0

win =PatientsWindow.PatientsWindow(getDataList(q), labels)
win.show()
app.exec_()