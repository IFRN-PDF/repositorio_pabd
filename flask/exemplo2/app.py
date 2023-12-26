# app.py
from flask import Flask, render_template, request, redirect, url_for
from database import get_projects_tasks, inserir_project, atualizar_project, remover_project

app = Flask(__name__)

@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        nome = request.form['nome']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']

        inserir_project(nome, data_inicio, data_fim)
        return redirect(url_for('projects_list'))
    return render_template('inserir.html')

@app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        atualizar_project(id, nome, data_inicio, data_fim)
        return redirect(url_for('projects_list'))
    return render_template('atualizar.html', id=id)

@app.route('/remover/<int:id>', methods=['GET', 'POST'])
def remover(id):
    remover_project(id)
    return redirect(url_for('projects_list'))


@app.route('/')
def projects_list():
    projects_tasks = get_projects_tasks()
    print(projects_tasks)
    return render_template('projects_tasks.html', projects_tasks=projects_tasks)

if __name__ == '__main__':
    app.run(debug=True)
