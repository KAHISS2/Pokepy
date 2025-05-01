import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self, file):
        self.file = file

    def conectionDatabase(self):
        conect = None
        try:
            conect = sqlite3.connect(self.file)
        except Error as er:
            return print(er)
        finally:
            return conect

    def searchDatabase(self, query):
        conect = self.conectionDatabase()
        cursor = conect.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conect.close()
        return res

    def crud(self, sql, execute=0, valores=None):
        conect = self.conectionDatabase()
        cursor = conect.cursor()
        if execute == 0:
            cursor.execute(sql)
        elif execute == 1:
            cursor.executemany(sql, valores)
        conect.commit()
        conect.close()
