# Importando as bibliotecas necessárias para trabalhar com bancos de dados PostgreSQL.
import psycopg2

# Configuração para conexão com o banco de dados
DB_NAME = "school_db"
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

def inserir_students(id, name, dob):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO students (id, name, dob) VALUES (%s, %s, %s)", 
                (id, name, dob)
            )
            conn.commit()

def inserir_courses(id, course_name, instructor, student_id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO courses (id, course_name, instructor, student_id) VALUES (%s, %s, %s, %s)", 
                (id, course_name, instructor, student_id)
            )
            conn.commit()

def buscar_dados(table):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table}")
            return cursor.fetchall()

if __name__ == "__main__":
    # Inserindo estudantes e cursos no banco de dados
    inserir_students(1, "Ana", "2005-05-15")
    inserir_students(2, "Bruno", "2004-03-22")
    inserir_students(3, "Carlos", "2006-08-14")
    inserir_students(4, "Daniela", "2005-11-03")
    inserir_students(5, "Eduardo", "2006-01-20")

    inserir_courses(1, "Matemática", "Prof. Jorge", 1)
    inserir_courses(2, "História", "Prof. Luiza", 3)

    # Buscando e imprimindo os estudantes e cursos inseridos
    students = buscar_dados("students")
    courses = buscar_dados("courses")

    print("Estudantes:")
    for student in students:
        print(student)

    print("\nCursos:")
    for course in courses:
        print(course)
