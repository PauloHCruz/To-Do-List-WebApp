from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret-key'

tasks = []

def get_tasks():
    if 'tasks' not in session:
        session['tasks'] = []
    return session['tasks']

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_title = request.form.get('task')
    if task_title:
        tasks = get_tasks()
        tasks.append({'title':task_title, 'done':False})
        session['tasks'] = tasks
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_index>', methods=['POST'])
def toggle(task_index):
    tasks = get_tasks()
    if 0 <= task_index <len(tasks):
        tasks[task_index]['done'] = not tasks[task_index]['done']
        session['tasks'] = tasks
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete(task_index):
    tasks = get_tasks()
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        session['tasks'] = tasks
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)