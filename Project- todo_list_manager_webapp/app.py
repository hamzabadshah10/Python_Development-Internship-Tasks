import gradio as gr

TaskList = []
CompletedTasks = set()
DeletedTasks = set()
AddedCount = 0
UpdatedCount = 0

def AddTask(TaskName, DueDate):
    global AddedCount
    if not TaskName:
        return "Task name cannot be empty.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]
    
    TaskList.append({
        "name": TaskName,
        "completed": False,
        "deleted": False,
        "due": DueDate or "No due date"
    })
    AddedCount += 1
    return "Task added successfully.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]

def CompleteTask(TaskID):
    try:
        TaskIndex = int(TaskID) - 1
        if 0 <= TaskIndex < len(TaskList):
            Task = TaskList[TaskIndex]
            if not Task["deleted"]:
                Task["completed"] = True
                CompletedTasks.add(TaskIndex)
                return "Task marked as completed.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]
        return "Invalid Task ID or already deleted.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]
    except:
        return "Enter a valid task number.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]

def DeleteTask(TaskID):
    try:
        TaskIndex = int(TaskID) - 1
        if 0 <= TaskIndex < len(TaskList):
            Task = TaskList[TaskIndex]
            if not Task["deleted"]:
                Task["deleted"] = True
                DeletedTasks.add(TaskIndex)
                return "Task deleted.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]
        return "Invalid Task ID or already deleted.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]
    except:
        return "Enter a valid task number.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]

def UpdateTask(TaskID, NewName):
    global UpdatedCount
    try:
        TaskIndex = int(TaskID) - 1
        if 0 <= TaskIndex < len(TaskList):
            Task = TaskList[TaskIndex]
            if not Task["deleted"]:
                Task["name"] = NewName
                UpdatedCount += 1
                return "Task updated.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]
        return "Invalid Task ID or already deleted.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]
    except:
        return "Enter a valid task number.", "", "", "", "", "", "", UpdateUI()[0], UpdateUI()[1]

def UpdateUI():
    Display = []
    for idx, task in enumerate(TaskList):
        if task["deleted"]:
            continue
        status = "Completed" if task["completed"] else "Pending"
        due = f"(Due: {task['due']})" if task['due'] != "No due date" else ""
        Display.append(f"{idx+1}. {task['name']} — {status} {due}")
    
    Stats = (
        f"📊 Total: {len(TaskList)} | "
        f"✅ Completed: {len(CompletedTasks)} | "
        f"🗑️ Deleted: {len(DeletedTasks)} | "
        f"➕ Added: {AddedCount} | "
        f"✏️ Updated: {UpdatedCount}"
    )
    return "\n".join(Display), Stats

# Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## <center><b>To-Do List Manager</b></center>")
    
    with gr.Row():
        with gr.Column():
            TaskName = gr.Textbox(label="Task Name")
            DueDate = gr.Textbox(label="Due Date")
            AddBtn = gr.Button("Add Task", variant="primary")

        with gr.Column():
            TaskDisplay = gr.Textbox(label="Task List", interactive=False, lines=10)
            StatsDisplay = gr.Markdown(
                "📊 Total: 0 | ✅ Completed: 0 | 🗑️ Deleted: 0 | ➕ Added: 0 | ✏️ Updated: 0"
            )

    with gr.Row():
        with gr.Column():
            CompID = gr.Textbox(label="Complete Task (Enter Task No.)")
            CompBtn = gr.Button("Mark Completed", variant="primary")
        with gr.Column():
            DelID = gr.Textbox(label="Delete Task (Enter Task No.)")
            DelBtn = gr.Button("Delete Task", variant="primary")

    with gr.Row():
        with gr.Column():
            UpID = gr.Textbox(label="Update Task (Enter Task No.)")
            NewName = gr.Textbox(label="New Task Name")
            UpdateBtn = gr.Button("Update Task", variant="primary")

    StatusBox = gr.Textbox(label="Status", interactive=False)

    # Event Bindings with textbox clearing after action
    AddBtn.click(AddTask, 
                 inputs=[TaskName, DueDate], 
                 outputs=[StatusBox, TaskName, DueDate, CompID, DelID, UpID, NewName, TaskDisplay, StatsDisplay])

    CompBtn.click(CompleteTask, 
                  inputs=CompID, 
                  outputs=[StatusBox, TaskName, DueDate, CompID, DelID, UpID, NewName, TaskDisplay, StatsDisplay])

    DelBtn.click(DeleteTask, 
                 inputs=DelID, 
                 outputs=[StatusBox, TaskName, DueDate, CompID, DelID, UpID, NewName, TaskDisplay, StatsDisplay])

    UpdateBtn.click(UpdateTask, 
                    inputs=[UpID, NewName], 
                    outputs=[StatusBox, TaskName, DueDate, CompID, DelID, UpID, NewName, TaskDisplay, StatsDisplay])

demo.launch()
