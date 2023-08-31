import psycopg2
from psycopg2 import sql

# Configuração de conexão
DB_NAME = "school_db"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

def conectar_servidor():
    return psycopg2.connect(
        dbname="postgres",
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

def conectar_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

def criar_db():
    conn = conectar_servidor()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
    cursor.close()
    conn.close()

def criar_tabelas(sql):    
    # Connect to our database and create the tables
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)

if __name__ == "__main__":
    criar_db()

    # SQL to create "students" table with a foreign key referencing "courses"
    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id  INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        dob DATE NOT NULL
    );
    """
    criar_tabelas(sql_create_students_table)
    
    sql_create_courses_table = """
    CREATE TABLE IF NOT EXISTS courses (
        id  INTEGER PRIMARY KEY,
        course_name VARCHAR(255) NOT NULL,
        instructor VARCHAR(255) NOT NULL,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
    """
    criar_tabelas(sql_create_courses_table)

