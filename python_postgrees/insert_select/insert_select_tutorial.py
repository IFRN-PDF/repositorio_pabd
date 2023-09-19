# Importando as bibliotecas necessárias para trabalhar com bancos de dados PostgreSQL.
import psycopg2

# Configuração para conexão com o banco de dados
DB_NAME = "tutorial_db"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

def conectar_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

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

# Função para buscar todos os dados de uma tabela.
def buscar_dados(table):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            # O comando SQL que busca todos os registros da tabela especificada.
            cursor.execute(f"SELECT * FROM {table}")
            return cursor.fetchall()

# A parte principal do nosso código.
# Quando executamos o script, tudo aqui é executado.
if __name__ == "__main__":
    # Inserindo alguns exemplos de projetos e tarefas no banco de dados.
    inserir_project(1, "Projeto Exemplo", "2023-09-01", "2023-12-31")
    inserir_task(1, "Tarefa 1", 1, 1, 1, "2023-09-01", "2023-10-01")
    inserir_task(2, "Tarefa 2", 2, 2, 1, "2023-10-02", "2023-11-01")
    inserir_task(3, "Tarefa 3", 3, 3, 1, "2023-11-02", "2023-12-01")

    # Buscando e imprimindo os dados que inserimos.
    projects = buscar_dados("projects")
    tasks = buscar_dados("tasks")

    print("Projetos:")
    for project in projects:
        print(project)
    
    print("\nTarefas:")
    for task in tasks:
        print(task)
