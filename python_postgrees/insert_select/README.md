# Exemplo de Inserçāo e Select

## Importações:

```python
import psycopg2
from psycopg2 import sql
```

O módulo `psycopg2` é uma biblioteca PostgreSQL para Python. Ele fornece uma maneira de se conectar e trabalhar com bancos de dados PostgreSQL.

## Configuração de Conexão:

```python
DB_NAME = "tutorial_db"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"
```

Estas são as credenciais e configurações usadas para se conectar ao banco de dados PostgreSQL. Certifique-se de que esses detalhes coincidam com sua instalação local do PostgreSQL.

## Função de Conexão:

```python
def conectar_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
```

Esta função cria e retorna uma conexão com o banco de dados usando as credenciais fornecidas.

## Funções de Inserção:

```python
def inserir_project(id, name, begin_date, end_date):
    ...
```

```python
def inserir_task(id, name, priority, status_id, project_id, begin_date, end_date):
    ...
```

Estas funções são usadas para inserir registros nas tabelas `projects` e `tasks`, respectivamente. Eles aceitam parâmetros que correspondem aos campos das respectivas tabelas.

## Função de Busca:

```python
def buscar_dados(table):
    ...
```

Esta função é usada para buscar todos os registros de uma tabela especificada. Ela retorna os registros como uma lista de tuplas.

## Main Execution:

```python
if __name__ == "__main__":
    ...
```

Esta seção do código é o ponto de entrada do script. Ele insere alguns dados de exemplo nas tabelas e, em seguida, recupera e imprime esses dados.

---

# Como Executar:

1. Certifique-se de ter o PostgreSQL instalado e em execução em sua máquina.
2. Instale a biblioteca `psycopg2` usando pip: `pip install psycopg2`.
3. Modifique as credenciais de conexão, se necessário.
4. Execute o script Python.


# 🚀 Atividade para você: Inserindo e Buscando Dados com PostgreSQL

## Objetivo:

Nesta atividade, você aprenderá a inserir e buscar informações nas tabelas `students` e `courses` usando Python e o módulo `psycopg2`.

## Instruções:

### 1. Inserção de Dados:

1. **Inserir Estudantes**:
    - Crie uma função chamada `inserir_student` que aceite `id`, `name` e `dob` como parâmetros.
    - Esta função deve inserir um novo estudante na tabela `students`.
    - Insira pelo menos 3 estudantes usando esta função.

2. **Inserir Cursos**:
    - Crie uma função chamada `inserir_course` que aceite `id`, `course_name`, `instructor` e `student_id` como parâmetros.
    - Esta função deve inserir um novo curso na tabela `courses`.
    - Insira pelo menos 5 cursos usando esta função. Certifique-se de associar alguns desses cursos aos estudantes que você inseriu anteriormente (usando o `student_id`).

### 2. Busca de Dados:

1. **Buscar Estudantes**:
    - Crie uma função chamada `buscar_students`.
    - Esta função deve buscar e retornar todos os estudantes da tabela `students`.
    - Imprima os estudantes retornados.

2. **Buscar Cursos**:
    - Crie uma função chamada `buscar_courses`.
    - Esta função deve buscar e retornar todos os cursos da tabela `courses`.
    - Imprima os cursos retornados.

## Dicas:

- Use o código fornecido como esqueleto para criar suas funções.
- Utilize o comando `INSERT INTO` para inserir os dados nas tabelas.
- Utilize o comando `SELECT` para buscar os dados das tabelas.
