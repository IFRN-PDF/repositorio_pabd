import psycopg2
from psycopg2 import sql

# Configuração de conexão
DB_NAME = "tutorial_db"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

# Função para conectar ao servidor Postgres (sem selecionar um banco de dados)
def conectar_servidor():
    return psycopg2.connect(
        dbname="postgres",
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

# Função para conectar ao nosso banco de dados
def conectar_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

# Função para criar um novo banco de dados
def criar_db():
    conn = conectar_servidor()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
    cursor.close()
    conn.close()

# Função para criar as tabelas
def criar_tabelas(sql):

    # Conectando e criando as tabelas
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)

if __name__ == "__main__":
    criar_db()
    
    # SQL para criar as tabelas
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text
    ); """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        name text NOT NULL,
        priority integer,
        status_id integer NOT NULL,
        project_id integer NOT NULL,
        begin_date text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    );"""
    
    criar_tabelas(sql_create_projects_table)
    criar_tabelas(sql_create_tasks_table)
