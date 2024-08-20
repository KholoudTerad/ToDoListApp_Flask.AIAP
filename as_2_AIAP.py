from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__, template_folder="templates")

# Initialize  list to store tasks. with one example
tasks = [{"content": "sample 1", "completed": False}]

# Home route to display the todo list
@app.route('/')
def index():
# Render the 'index.html' template and pass the 'tasks' list to it  
    return render_template('index.html', tasks=enumerate(tasks))
  

# Add a task
@app.route('/add_task', methods=['POST'])
def add_task():
# Extract the task content from the form submitted by the user
    task_content = request.form['content']
    # Append the new task to the 'tasks' list
    tasks.append({"content": task_content, 'completed': False})
    # Redirect the user to the home route after adding the task
    return redirect(url_for('index'))

# Remove a task
@app.route('/delete_task/<int:index>', methods=['GET'])
def delete_task(index):
 # Check if the index is within the range of valid indices in the 'tasks' list
    if 0 <= index < len(tasks):
 # Delete the task at the specified index from the 'tasks' list
        del tasks[index]
    # Redirect the user to the home route after deleting the task
    return redirect(url_for('index'))

# Mark a task as completed
@app.route('/complete_task/<int:index>', methods=['GET'])
def complete_task(index):
    # Check if the index is within the range of valid indices in the 'tasks' list
    if 0 <= index < len(tasks):
        # Mark the task at the specified index as completed
        tasks[index]['completed'] = True
    # Redirect the user to the home route after marking the task as completed
    return redirect(url_for('index'))

#  Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)