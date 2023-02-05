import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ cria uma conexão de banco de dados com o banco de dados SQLite
         especificado por db_file
     :param db_file: arquivo de banco de dados
     :return: Objeto de conexão ou Nenhum
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def execute_select(conn,sql_select):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(sql_select)

    return cur.fetchall()


def show_rows(titles,rows,qtd=10):
    """mostrando as 10 primeiras linhas"""
    print('| {:1} | {:} |'.format(*titles))
    
    for row in rows[:qtd]:
        print('| {:1} | {:} |'.format(*row))

