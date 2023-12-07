import psycopg2
from psycopg2 import sql

# Configuração de conexão
DB_NAME = "tutorial_db"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

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
    # Função para conectar ao servidor Postgres (sem selecionar um banco de dados)
    def conectar_servidor():
        return psycopg2.connect(
            dbname="postgres",
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
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
# Função para inserir um novo projeto no banco de dados.
def inserir_project(id, name, begin_date, end_date):
    # Conectando ao banco de dados.
    with conectar_db() as conn:
        # Criando um "cursor". Pense nele como um "dedo" que executa ações no banco de dados.
        with conn.cursor() as cursor:
            # O comando SQL que insere os dados na tabela "projects".
            cursor.execute(
                "INSERT INTO projects (id, name, begin_date, end_date) VALUES (%s, %s, %s, %s)", 
                (id, name, begin_date, end_date)
            )
            # Salvando as alterações.
            conn.commit()
# Função para inserir uma nova tarefa no banco de dados.
def inserir_task(id, name, priority, status_id, project_id, begin_date, end_date):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO tasks (id, name, priority, status_id, project_id, begin_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                (id, name, priority, status_id, project_id, begin_date, end_date)
            )
            conn.commit()

"""Consulta e retorna todos os projetos e suas tarefas relacionadas."""
def get_projects_tasks():
    
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
    SELECT projects.id, projects.name, tasks.name, tasks.priority, tasks.status_id
    FROM projects INNER
    JOIN tasks ON projects.id = tasks.project_id
    """)
    projects_tasks = cur.fetchall()
    cur.close()
    conn.close()
    return projects_tasks

#Somente rode esse aquivo se nāo tiver dados no seu banco
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
    # Inserindo alguns exemplos de projetos e tarefas no banco de dados.
    inserir_project(1, "Projeto Exemplo", "2023-09-01", "2023-12-31")
    inserir_task(1, "Tarefa 1", 1, 1, 1, "2023-09-01", "2023-10-01")
    inserir_task(2, "Tarefa 2", 2, 2, 1, "2023-10-02", "2023-11-01")
    inserir_task(3, "Tarefa 3", 3, 3, 1, "2023-11-02", "2023-12-01")
