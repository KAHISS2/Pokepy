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


    def searchPerPokemons(self, query, treeview):
        conect = self.conectionDatabase()
        cursor = conect.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conect.close()
        
        for i in res:
            treeview.insert("", "end", values=i[0:])

    def insertPokemonToDatabase(self, sql):
        conect = self.conectionDatabase()
        cursor = conect.cursor()
        cursor.execute(sql)
        conect.commit()
        conect.close()
