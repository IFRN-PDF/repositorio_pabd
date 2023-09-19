import psycopg2

# Configurações de conexão
DB_NAME = "tutorial_db"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

# Função para conectar ao banco de dados
def conectar_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

# Função para atualizar um campo específico em uma tabela específica
def atualizar_dado(tabela, campo, valor, id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            query = f"UPDATE {tabela} SET {campo} = %s WHERE id = %s"
            cursor.execute(query, (valor, id))
            conn.commit()

# Função para remover um registro de uma tabela com base em um ID
def remover_por_id(tabela, id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            query = f"DELETE FROM {tabela} WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()

def buscar_dados(table):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            # O comando SQL que busca todos os registros da tabela especificada.
            cursor.execute(f"SELECT * FROM {table}")
            return cursor.fetchall()

def print_dados():
    projects = buscar_dados("projects")
    tasks = buscar_dados("tasks")

    print("Projetos:")
    for project in projects:
        print(project)
    
    print("\nTarefas:")
    for task in tasks:
        print(task)
# Testando as funções
if __name__ == "__main__":
    print("**Dados antes:")
    print_dados()

    # Atualizando o nome de um projeto com ID = 1
    atualizar_dado('projects', 'name', 'Projeto Atualizado', 1)

    # Removendo uma tarefa com ID = 2
    remover_por_id('tasks', 2)
    
    print("**Dados depois:")
    print_dados()
