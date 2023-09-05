# Introdução ao PostgreSQL com Python

Olá, jovem desenvolvedor(a)! Vamos juntar o conhecimento de SQL CREATE e python para desenvolver nossa primeira aplicaçāo com acesso a banco de dados.

## O que é PostgreSQL?

PostgreSQL, carinhosamente chamado de Postgres, é um sistema de gerenciamento de banco de dados relacional (RDBMS) gratuito e de código aberto. É conhecido por sua robustez, extensibilidade e conformidade com padrões. Em palavras simples: é onde você pode armazenar, organizar e recuperar seus dados de forma eficiente!

## Por que usar PostgreSQL?

1. **Gratuito e de código aberto:** Você não precisa pagar nada para usá-lo.
2. **Extensível:** Você pode criar suas próprias funções, tipos de dados e mais.
3. **Conformidade com padrões:** Adere aos padrões SQL, garantindo que você aprenda SQL da maneira "certa".

## Como instalar o PostgreSQL?

1. **Windows:** [Baixe o instalador oficial](https://www.postgresql.org/download/windows/)
2. **Mac:** Use o Homebrew: `brew install postgresql`
3. **Linux:** Depende da sua distribuição, mas geralmente `sudo apt-get install postgresql` para sistemas baseados em Debian.

Após a instalação, você pode iniciar o Postgres com o comando `pg_ctl start`.

## Preparando o ambiente Python

Para interagir com o Postgres usando Python, precisamos de uma biblioteca chamada `psycopg2`. Instale-a com:

```bash
pip install psycopg2
```

- Clique aqui para ver o [Exemplo create_table.py](create/README.md)

# PGAdmin: A Ferramenta Gráfica para o PostgreSQL

![Logo PGAdmin](https://api.mogenius.com/file/id/9b0934ab-599b-4ab7-8e65-02895f84a98c)

Depois de falar sobre o PostgreSQL, é impossível não mencionar o **pgAdmin**. Ele é a ferramenta de administração e gestão mais popular para o PostgreSQL, e o melhor de tudo: é gratuita e de código aberto!

## O que é o pgAdmin?

O **pgAdmin** é uma plataforma de administração e gestão para o PostgreSQL. Ela permite que você interaja com seu banco de dados de forma visual, facilitando tarefas como:

- Criar e modificar tabelas
- Visualizar dados em tabelas
- Executar consultas SQL
- Gerenciar permissões e usuários
- E muito mais!

Tudo isso através de uma interface amigável e intuitiva.

## Por que usar o pgAdmin?

1. **Interface Gráfica:** Para quem não está acostumado com a linha de comando, o pgAdmin oferece uma maneira fácil e visual de gerenciar bancos de dados.
2. **Multiplataforma:** Funciona em Windows, Mac e Linux.
3. **Poderoso:** Apesar de ser visual, o pgAdmin é extremamente poderoso e pode lidar com praticamente qualquer tarefa relacionada ao PostgreSQL.
4. **Desenvolvimento de Consultas:** Possui um editor SQL integrado para você testar suas consultas.

## Como instalar o pgAdmin?

1. **Windows:** [Baixe o instalador oficial](https://www.pgadmin.org/download/pgadmin-4-windows/)
2. **Mac:** Use o Homebrew: `brew install pgadmin4`
3. **Linux:** Depende da sua distribuição, mas geralmente `sudo apt-get install pgadmin4` para sistemas baseados em Debian.

## Primeiros passos com o pgAdmin:

1. **Inicie o pgAdmin** após a instalação.
2. **Conecte-se ao seu servidor PostgreSQL:** Na primeira vez que você executar o pgAdmin, ele pedirá que você se conecte a um servidor PostgreSQL. Use as credenciais do seu servidor local (geralmente "localhost" com seu nome de usuário e senha).
3. **Navegue pelo painel lateral:** Você verá seus bancos de dados, esquemas, tabelas e outros objetos.
4. **Crie e execute consultas:** Use o editor SQL para criar e testar suas consultas.

Agora, com o **pgAdmin** à sua disposição, você tem uma ferramenta poderosa para gerenciar e visualizar seus bancos de dados. Recomendo que brinque um pouco com ele para se familiarizar e descobrir todas as suas funcionalidades incríveis! 🌟
