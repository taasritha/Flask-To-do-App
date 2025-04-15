from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    global task_id_counter
    if request.method == 'POST':
        data = request.json
        task = {'id': task_id_counter, 'task': data['task'], 'done': False}
        tasks.append(task)
        task_id_counter += 1
        return jsonify(task), 201
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = data['task']
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': 'Task deleted'})

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



