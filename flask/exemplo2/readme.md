# Explicação do Template `projects_tasks.html`

O arquivo `projects_tasks.html` é um template HTML usado em uma aplicação Flask para exibir projetos e tarefas em uma tabela. Abaixo, é detalhado o funcionamento de cada parte do template:

## Estrutura Básica

```html
<!DOCTYPE html>
<html lang="en">
<head>
    ...
</head>
<body>
    ...
</body>
</html>
```

- `<!DOCTYPE html>`: Declara que este documento é um documento HTML5.
- `<html lang="en">`: O elemento raiz de um documento HTML com o atributo `lang` definido como inglês (`en`).

## Cabeçalho do Documento (Head)

```html
<head>
    <meta charset="UTF-8">
    <title>Projects and Tasks</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
```

- `<meta charset="UTF-8">`: Define a codificação de caracteres para o documento HTML como UTF-8, que inclui a maioria dos caracteres de todos os idiomas escritos.
- `<title>Projects and Tasks</title>`: Define o título do documento, que é exibido na aba do navegador.
- `<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">`: Vincula uma folha de estilo CSS externa ao documento. O `url_for` é uma função do Flask para gerar URLs para arquivos estáticos, garantindo o caminho correto para o arquivo `style.css`.

## Corpo do Documento (Body)

```html
<body>
    <table>
        ...
    </table>
</body>
```

- `<body>`: Contém o conteúdo visível da página da web.

## Tabela de Projetos e Tarefas

```html
<table>
    <thead>
        <tr>
            <th>Project ID</th>
            ...
        </tr>
    </thead>
    <tbody>
        {% for project_id, project_name, task_name, task_priority, task_status in projects_tasks %}
        <tr>
            <td>{{ project_id }}</td>
            ...
        </tr>
        {% endfor %}
    </tbody>
</table>
```

- `<table>`: Define uma tabela HTML.
- `<thead>`: Define um cabeçalho de tabela contendo células de cabeçalho (`<th>`) que representam os títulos das colunas.
- `<tbody>`: Contém o corpo da tabela, onde os dados são realmente inseridos.
- `{% for ... in projects_tasks %}`: Um loop do Jinja2 que itera sobre a coleção `projects_tasks` passada do Flask.
- `<tr>`: Define uma linha da tabela.
- `<td>`: Define uma célula de dados da tabela.
- `{{ project_id }}`, `{{ project_name }}`, ...: São variáveis do Jinja2 que são preenchidas com os dados de cada projeto e tarefa.

- Este template é renderizado pelo Flask quando você visita a rota correspondente (`/`). 
- O Flask passa a variável `projects_tasks` para o template, que contém os dados dos projetos e tarefas, e o template usa a sintaxe do Jinja2 para iterar sobre esses dados e apresentá-los em uma tabela HTML.
