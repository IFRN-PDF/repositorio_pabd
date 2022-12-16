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


def insert_project(conn, project):
    """
    Inserir um novo projeto na tabela de projetos
     :param conn:
     :param projeto:
     :return: ID do projeto
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    #pegar o cursor
    cur = conn.cursor()
    #executar sql
    cur.execute(sql, project)
    #confirmando a transação atual
    conn.commit()
    #retorna o ultimo id salvo
    return cur.lastrowid


def insert_task(conn, task):
    """
    Inserir uma nova task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main():
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Projeto bacana com SQLite & Python', '2015-01-01', '2015-01-30');
        project_id = insert_project(conn, project)

        # tasks
        task_1 = ('Analizar os pre-requistos do app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirmar como o usuario as prioridades', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        insert_task(conn, task_1)
        insert_task(conn, task_2)


if __name__ == '__main__':
    main()