'''
Exemplo de criaçāo de tabelas.
Segue o diagrama que está sendo criado:
https://imgur.com/lez61sH

para checar no banco use os comandos:
sqlite3 pythonsqlite.db
sqlite> .tables
'''
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

def create_table(conn, create_table_sql):
    """ cria uma tabela a partir da instrução create_table_sql
     :param conn: Objeto de conexão
     :param create_table_sql: uma instrução CREATE TABLE
     :Retorna: nada
    """
    try:
        c = conn.cursor()
        '''chamamos o método execute() do objeto Cursor para
        executar a instrução CREATE TABLE.'''
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main():
    database = "pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()