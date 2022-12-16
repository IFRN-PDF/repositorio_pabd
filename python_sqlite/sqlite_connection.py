'''
Teste de criaçāo de banco
instlar o sqlite baixa baixar o instalador:
https://sqlite.org/2022/sqlite-dll-win64-x64-3400000.zip
'''

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ Criar conexāo com o banco sqlite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    #nome do arquivo em que os dados do banco estarāo armazenados
    create_connection("pythonsqlite.db")