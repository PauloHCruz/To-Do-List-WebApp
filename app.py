from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_title = request.form.get('task')
    if task_title:
        tasks.append({'title':task_title, 'done':False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_index>', methods=['POST'])
def toggle(task_index):
    if 0 <= task_index <len(tasks):
        tasks[task_index]['done'] = not tasks[task_index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)