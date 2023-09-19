# README

## Atualização e Remoção de Registros em PostgreSQL usando Python

Este guia aborda como usar Python para interagir com um banco de dados PostgreSQL, especificamente para atualizar e remover registros. 

### Visão Geral

O script fornece duas funções essenciais:
1. `atualizar_dado`: Atualiza um valor específico em uma tabela.
2. `remover_por_id`: Remove um registro de uma tabela com base no ID.

### Configuração de Conexão:

```python
DB_NAME = "tutorial_db"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"
```

**Conceitos Básicos**:
- **Configuração de Conexão**: Estas são as credenciais para se conectar ao banco de dados. Eles atuam como a "identidade" para o seu banco de dados e devem ser mantidos em segurança.

### Conectando ao Banco de Dados:

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

**Conceitos Básicos**:
- **Conexão**: Uma conexão é como abrir uma porta para o seu banco de dados. É necessário estabelecer uma conexão antes de executar qualquer operação no banco de dados.

### Atualizando Dados:

```python
def atualizar_dado(tabela, campo, valor, id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            query = f"UPDATE {tabela} SET {campo} = %s WHERE id = %s"
            cursor.execute(query, (valor, id))
            conn.commit()
```

**Conceitos Básicos**:
- **SQL Update**: A operação `UPDATE` permite modificar dados existentes em uma tabela. A cláusula `WHERE` especifica qual registro ou registros devem ser atualizados.
- **Placeholder (%s)**: É uma prática recomendada não concatenar ou interpolar diretamente os valores nas consultas para evitar ataques de injeção SQL. Em vez disso, usamos placeholders e passamos os dados separadamente.

### Removendo Dados:

```python
def remover_por_id(tabela, id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            query = f"DELETE FROM {tabela} WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
```

**Conceitos Básicos**:
- **SQL Delete**: A operação `DELETE` permite remover registros de uma tabela. Assim como o `UPDATE`, geralmente é usado com a cláusula `WHERE` para especificar quais registros devem ser excluídos.

### Pontos Adicionais:

- **Commit**: Após executar uma operação que modifica o banco de dados (como `INSERT`, `UPDATE`, ou `DELETE`), é essencial "commitar" (ou confirmar) essas mudanças. Isso garante que as alterações sejam salvas no banco de dados.
- **Cursor**: Pense em um cursor como um 'dedo' que aponta e interage com o banco de dados. É usado para executar comandos e buscar resultados.

# Atividade Prática: Gerenciando Projetos e Tarefas

## Introdução:

Você aprendeu como criar, atualizar e remover registros de um banco de dados usando Python e PostgreSQL. Agora, vamos aplicar esse conhecimento ao gerenciamento de projetos e tarefas!

### Contexto:

Você é o coordenador de TI de uma startup em crescimento. A equipe usa um sistema simples baseado em banco de dados para rastrear projetos e tarefas associadas. Durante uma revisão, você descobriu que alguns dados foram inseridos erroneamente e algumas tarefas estão desatualizadas. Sua missão é corrigir essas discrepâncias.

## Tarefa:

1. **Inserção**:
    - Adicione um novo projeto chamado "Desenvolvimento de App Móvel".
    - Adicione três tarefas associadas a esse projeto, como "Design da Interface do Usuário", "Desenvolvimento do Backend" e "Testes".

2. **Atualização**:
    - Um dos projetos foi renomeado. Atualize o nome de "Projeto Exemplo" para "Projeto Piloto".
    - A prioridade de uma tarefa foi alterada. Atualize a prioridade da "Tarefa 1" para 3.

3. **Remoção**:
    - Um projeto piloto foi cancelado. Remova o projeto chamado "Projeto Piloto" e todas as tarefas associadas a ele.

## Requisitos:

- Utilize funções Python para inserção, atualização e remoção de registros.
- Após cada operação, verifique no banco de dados e imprima o resultado para garantir que a operação foi bem-sucedida.

## Dicas:

- Ao lidar com a remoção de projetos, lembre-se das dependências. Ao remover um projeto, suas tarefas associadas também devem ser removidas.
- Utilize o comando `SELECT` para verificar as alterações após as operações de atualização e remoção.

---

## Conclusão

Este guia forneceu uma visão detalhada de como usar Python para atualizar e remover registros de um banco de dados PostgreSQL. Ao entender e usar esses conceitos, você estará bem equipado para gerenciar e manipular bancos de dados de forma eficaz e segura.

