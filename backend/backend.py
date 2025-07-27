from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []
task_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global task_counter
    task_data = request.json
    task = {
        'id': task_counter,
        'task': task_data.get('task', '')
    }
    tasks.append(task)
    task_counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': 'deleted'})

if __name__ == '__main__':
    app.run(port=5001, debug=True)

