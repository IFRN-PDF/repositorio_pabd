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

# Função para inserir dados em projects
def inserir_projects(dados):
    conn = conectar_db()
    cursor = conn.cursor()
    query = "INSERT INTO projects (id, name, begin_date, end_date) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, dados)
    conn.commit()
    cursor.close()
    conn.close()

# Função para inserir dados em tasks
def inserir_tasks(dados):
    conn = conectar_db()
    cursor = conn.cursor()
    query = "INSERT INTO tasks (id, name, priority, status_id, project_id, begin_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, dados)
    conn.commit()
    cursor.close()
    conn.close()

# Função para executar uma consulta SELECT JOIN
def executar_select(query):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

if __name__ == "__main__":
   # Dados para inserir em projects
    dados_projects = [
        (1, "Projeto Alpha", "2023-01-01", "2023-12-31"),
        (2, "Projeto Beta", "2023-02-01", "2023-11-30"),
        (3, "Projeto Gamma", "2023-03-01", "2023-10-31"),
        (4, "Projeto Delta", "2023-04-01", "2023-09-30"),
        (5, "Projeto Epsilon", "2023-05-01", "2023-08-31")
    ]
    # Dados para inserir em tasks
    dados_tasks = [
    # Tarefas para Projeto Alpha
    (1, "Tarefa Alpha 1", 1, 1, 1, "2023-01-10", "2023-01-20"),
    (2, "Tarefa Alpha 2", 2, 1, 1, "2023-02-10", "2023-02-20"),
    (3, "Tarefa Alpha 3", 3, 1, 1, "2023-03-10", "2023-03-20"),
    
    # Tarefas para Projeto Beta
    (4, "Tarefa Beta 1", 1, 1, 2, "2023-02-15", "2023-03-15"),
    (5, "Tarefa Beta 2", 2, 1, 2, "2023-03-15", "2023-04-15"),
    (6, "Tarefa Beta 3", 3, 1, 2, "2023-04-15", "2023-05-15"),
    (7, "Tarefa Beta 4", 4, 1, 2, "2023-05-15", "2023-06-15"),
    (8, "Tarefa Beta 5", 5, 1, 2, "2023-06-15", "2023-07-15"),

    # Tarefas para Projeto Delta
    (9, "Tarefa Delta 1", 1, 1, 4, "2023-04-20", "2023-05-20"),

    # Tarefas para Projeto Epsilon
    (10, "Tarefa Epsilon 1", 1, 1, 5, "2023-05-01", "2023-05-10"),
    (11, "Tarefa Epsilon 2", 2, 1, 5, "2023-05-11", "2023-05-20"),
    (12, "Tarefa Epsilon 3", 3, 1, 5, "2023-05-21", "2023-05-30"),
    (13, "Tarefa Epsilon 4", 4, 1, 5, "2023-06-01", "2023-06-10"),
    (14, "Tarefa Epsilon 5", 5, 1, 5, "2023-06-11", "2023-06-20"),
    (15, "Tarefa Epsilon 6", 6, 1, 5, "2023-06-21", "2023-06-30"),
    (16, "Tarefa Epsilon 7", 7, 1, 5, "2023-07-01", "2023-07-10"),
    (17, "Tarefa Epsilon 8", 8, 1, 5, "2023-07-11", "2023-07-20"),
    (18, "Tarefa Epsilon 9", 9, 1, 5, "2023-07-21", "2023-07-30"),
    (19, "Tarefa Epsilon 10", 10, 1, 5, "2023-08-01", "2023-08-10")
    ]

    inserir_projects(dados_projects)
    inserir_tasks(dados_tasks)

    query = """
    SELECT *
    FROM tasks
    """
    resultados = executar_select(query)
    for resultado in resultados:
        print(resultado)
    
    #Crie 4 queries para cada join visto em aula para as tabelas projects e tasks.
    