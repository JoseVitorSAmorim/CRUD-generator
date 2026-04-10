import sqlite3

class Tabela:
    def __init__(self, db = ""):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        return  self.conn, self.cursor
    
    def criar_db(self, tabela, coluna, tipo):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS (tabela)(
                id INTERGER PRIMARY KEY AUTOINCREMENT,
                (coluna) (tipo)
                ); VALUES(?, ?, ?)''', (tabela, coluna, tipo))
        self.conn.commit()
        self.conn.close()