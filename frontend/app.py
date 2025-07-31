from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
BACKEND_URL = 'http://localhost:5001'
@app.route('/tasks')
def show_tasks():
    # similar logic as your index() function
    if request.method == 'POST':
        task = request.form['task']
        requests.post(f'{BACKEND_URL}/tasks', json={'task': task})
        return redirect('/')
    # Get tasks from backend API
    resp = requests.get(f'{BACKEND_URL}/tasks')
    tasks = resp.json()
    return render_template('index.html', tasks=tasks)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        requests.post(f'{BACKEND_URL}/tasks', json={'task': task})
        return redirect('/')
    # Get tasks from backend API
    resp = requests.get(f'{BACKEND_URL}/tasks')
    tasks = resp.json()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    requests.delete(f'{BACKEND_URL}/tasks/{task_id}')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
