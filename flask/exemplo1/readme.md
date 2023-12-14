# Aplicativos Flask: Hello World e HTML Rendering

Este repositório contém dois exemplos de aplicativos Flask. O primeiro retorna uma simples mensagem de texto e o segundo renderiza uma página HTML.

## Estrutura do Código

- `hello_app.py`: Retorna "Hello, World!" na rota raiz.
- `html_app.py`: Renderiza uma página HTML localizada dentro da pasta `templates`.
- `templates/`: Contém os arquivos HTML que serão renderizados pelo Flask.
  - `index.html`: A página HTML que `html_app.py` irá renderizar.
- `templates/css` : Contém os arquivos CSS.

## Como Executar

### hello_app.py

Para executar o aplicativo que retorna "Hello, World!", basta seguir os passos abaixo:

1. **Execute o Aplicativo**:

   ```bash
   python hello_app.py
   ```

2. **Acesso**:

   Abra seu navegador e vá para `http://localhost:5000` para ver a mensagem.

### html_app.py

Para executar o aplicativo que renderiza uma página HTML:

1. **Execute o Aplicativo**:

   ```bash
   python html_app.py
   ```

2. **Acesso**:

   Abra seu navegador e vá para `http://localhost:5000` para ver a página HTML renderizada.


## Requisitos

- Python 3.x
- Flask
  - instalar: `pip install flask`

---

## Entendendo `{{ ... }}` e `url_for` em Templates Flask com Jinja2

### Templates Jinja2
- Utilizados no Flask para inserir dados dinâmicos em HTML.
- Processados pelo servidor antes de serem enviados ao cliente.

### Sintaxe `{{ ... }}`
- Delimitadores que indicam expressões a serem avaliadas pelo servidor.
- Substituem variáveis pelos valores reais no momento da renderização.

### Tag `<link>` e Atributos
- `<link>`: Elemento HTML para vincular recursos externos, como CSS.
- `rel="stylesheet"`: Especifica que o recurso vinculado é uma folha de estilo.

### Função `url_for`
- Gera URLs dinamicamente para arquivos estáticos no Flask.
- Evita a necessidade de codificar URLs estáticas, adaptando-se a mudanças de estrutura.

### Endpoint `static`
- Referência especial no Flask para a pasta `static` do projeto.
- Usado por `url_for` para localizar arquivos estáticos.

### Argumento `filename`
- Define o caminho específico do arquivo dentro da pasta `static`.
- `url_for('static', filename='css/style.css')` gera `/static/css/style.css`.

### Vantagens de `url_for`
- Geração automática de URLs corretas independente do ambiente.
- Facilita a manutenção e atualização de links para recursos estáticos.
- Aumenta a segurança evitando erros comuns de caminho de arquivo.

### Processamento do Template
- `{{ ... }}` é substituído pela URL gerada no HTML final.
- O navegador solicita o CSS usando a URL fornecida pelo servidor.

### Flexibilidade e Segurança
- O Flask gerencia os caminhos de arquivos estáticos, garantindo flexibilidade.
- Protege contra problemas de segurança relacionados a caminhos de arquivos incorretos.


