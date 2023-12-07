# app.py
from flask import Flask, render_template
from database import get_projects_tasks

app = Flask(__name__)


@app.route('/')
def projects_list():
    projects_tasks = get_projects_tasks()
    return render_template('projects_tasks.html', projects_tasks=projects_tasks)

if __name__ == '__main__':
    app.run(debug=True)
