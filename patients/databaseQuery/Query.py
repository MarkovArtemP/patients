from PyQt4.QtSql import *

from databaseQuery.ErrorMessage import ErrorDialog


class Query:
    class __Query:
        def __init__(self, parameters=None):
            self.db = None
            self.header = []
            self.data_list = []
            self.query = None
            if parameters is None:
                ErrorDialog('No parameters')
            else:
                self.query = self.getQuery(parameters)
                if self.query is None:
                    ErrorDialog('Database error', self.db.lastError().text())
                else:
                    self.execQuery()

        def getQuery(self, parameters):
            self.db = QSqlDatabase.addDatabase("QMYSQL")
            self.db.setHostName(parameters['host'])
            try:
                self.db.setPort(int(parameters['port']))
            except:
                return None
            self.db.setDatabaseName(parameters['database'])
            self.db.setUserName(parameters['username'])
            self.db.setPassword(parameters['password'])
            if self.db.open():
                return QSqlQuery(self.db)
            else:
                return None

        def execQuery(self, where="TRUE"):
            #TODO delete this
            self.query.exec_(
                    "SELECT x.* FROM ( SELECT " +
                    "Client.lastName AS 'Фамилия', " +
                    "Client.firstName AS 'Имя', " +
                    "Client.patrName AS 'Отчество', " +
                    "DATE_FORMAT(Client.birthDate, '%d.%m.%Y') AS 'Дата_рождения', " +
                    "((YEAR(CURRENT_DATE) - YEAR(Client.birthDate)) - (DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(Client.birthDate, '%m%d'))) AS 'Возраст', " +
                    "IF(Client.sex = 1, 'Муж', 'Жен' ) AS 'Пол', " +
                    "rbDocumentType.name AS 'Тип_документа', " +
                    "ClientDocument.serial AS 'Серия', " +
                    "ClientDocument.number AS 'Номер', " +
                    "DATE_FORMAT(ClientDocument.date, '%d.%m.%Y') AS 'Дата_выдачи', " +
                    "rbPolicyType.name AS 'Тип_полиса', " +
                    "ClientPolicy.serial AS 'Серия_полиса', " +
                    "ClientPolicy.number AS 'Номер_полиса', " +
                    "DATE_FORMAT(ClientPolicy.begDate, '%d.%m.%Y') AS 'Дата_начала', " +
                    "DATE_FORMAT(ClientPolicy.endDate, '%d.%m.%Y') AS 'Дата_окончания', " +
                    "ClientPolicy.name AS 'Name', " +
                    "ClientPolicy.note AS 'Note' " +
                    "FROM Client " +
                    "LEFT JOIN ClientDocument ON ClientDocument.client_id = Client.id " +
                    "LEFT JOIN ClientPolicy ON ClientPolicy.client_id = Client.id " +
                    "LEFT JOIN rbDocumentType ON rbDocumentType.id = ClientDocument.documentType_id " +
                    "LEFT JOIN rbPolicyType ON rbPolicyType.id = ClientPolicy.policyType_id " +
                    ") x " +
                    "WHERE " + where + " ;")
            record = self.query.record()
            self.header = []
            for i in range(0, record.count()):
                self.header.append(record.fieldName(i))

            self.data_list = []
            index = 0
            while self.query.next():
                row = []
                for i in range(0, self.query.record().count()):
                    row.append(self.query.value(i))
                index += 1
                self.data_list.append(tuple(row))

    instance = None

    def __init__(self, parameters=None):
        if not Query.instance:
            Query.instance = Query.__Query(parameters)

    def refreshParameters(self, parameters):
        Query.instance = None
        Query(parameters)

    def getDataList(self):
        return self.instance.data_list

    def getHeader(self):
        return self.instance.header

    def refreshQuery(self, where='TRUE'):
        self.instance.execQuery(where)
