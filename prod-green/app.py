from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store tasks in memory (in a real app, you'd use a database)
tasks = []

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Task Manager</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .task-form { margin-bottom: 20px; }
            .task-list { list-style: none; padding: 0; }
            .task-item { padding: 10px; border: 1px solid #ddd; margin-bottom: 5px; }
        </style>
    </head>
    <body>
        <h1>Task Manager</h1>
        <div class="task-form">
            <h2>Add New Task</h2>
            <form id="taskForm" onsubmit="addTask(event)">
                <input type="text" id="taskInput" placeholder="Enter task description" required>
                <button type="submit">Add Task</button>
            </form>
        </div>
        <div>
            <h2>Tasks</h2>
            <ul id="taskList" class="task-list"></ul>
        </div>
        <script>
            function addTask(event) {
                event.preventDefault();
                const taskInput = document.getElementById('taskInput');
                const task = taskInput.value;
                
                fetch('/add_task', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({task: task}),
                })
                .then(response => response.json())
                .then(data => {
                    taskInput.value = '';
                    loadTasks();
                });
            }

            function loadTasks() {
                fetch('/tasks')
                    .then(response => response.json())
                    .then(tasks => {
                        const taskList = document.getElementById('taskList');
                        taskList.innerHTML = '';
                        tasks.forEach(task => {
                            const li = document.createElement('li');
                            li.className = 'task-item';
                            li.textContent = task;
                            taskList.appendChild(li);
                        });
                    });
            }

            // Load tasks when page loads
            loadTasks();
        </script>
    </body>
    </html>
    '''

@app.route('/add_task', methods=['POST'])
def add_task():
    task_data = request.get_json()
    task = task_data.get('task')
    if task:
        tasks.append(task)
        return jsonify({"status": "success", "message": "Task added"}), 201
    return jsonify({"status": "error", "message": "No task provided"}), 400

@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)

@app.route('/task/<int:task_id>')
def get_task(task_id):
    if 0 <= task_id < len(tasks):
        return jsonify({"task": tasks[task_id]})
    return jsonify({"status": "error", "message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)