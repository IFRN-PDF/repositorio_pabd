'''
Exemplo de insert dados nas tabelas.
Segue o diagrama que está sendo criado:
https://imgur.com/lez61sH
para checar no banco use os comandos:
sqlite3 pythonsqlite.db
sqlite> .header on
sqlite> .mode column
sqlite> SELECT * FROM projects;
sqlite> SELECT * FROM tasks;
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

def script_to_create_tables(database):
    sql_create_cidade_table = """ CREATE TABLE IF NOT EXISTS cidade (
                                        id_cidade integer PRIMARY KEY,
                                        nome text NOT NULL
                                    ); """

    sql_create_curso_table = """ CREATE TABLE IF NOT EXISTS curso (
                                                id_curso integer PRIMARY KEY,
                                                nome text NOT NULL
                                            ); """

    sql_create_aluno_table = """ CREATE TABLE IF NOT EXISTS aluno (
                                            id_aluno integer PRIMARY KEY,
                                            nome text NOT NULL,
                                            email text NOT NULL,
                                            id_cidade integer,
                                            id_curso integer,
                                            FOREIGN KEY (id_cidade) REFERENCES cidade (id_cidade),
                                            FOREIGN KEY (id_curso) REFERENCES curso (id_curso)
                                        ); """ 
# create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_cidade_table)

        create_table(conn, sql_create_curso_table)

        create_table(conn, sql_create_aluno_table)
    else:
        print("Error! cannot create the database connection.")                                        

def insert_cidade(conn, cidade):
    """
    Inserir uma nova cidade
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO cidade(nome) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, cidade)
    conn.commit()
    return cur.lastrowid

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
    database = "atv2.db"
    #script_to_create_tables(database)
    conn = create_connection(database)
    with conn:
        insert_cidade(conn,("Natal",))
    
if __name__ == '__main__':
    main()