import datetime


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "не выполнено"
        self.creation_date = datetime.datetime.now()

    def mark_as_done(self):
        self.status = "выполнено"

    def mark_as_undone(self):
        self.status = "не выполнено"

    def edit_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Название: {self.title}\nОписание: {self.description}\nСтатус: {self.status}\nДата создания: {self.creation_date}"


class TaskList:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            return None

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_all_tasks(self):
        return self.tasks

    def __len__(self):
        return len(self.tasks)


def log_activity(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arguments = ", ".join([repr(arg) for arg in args] + [f"{key}={value!r}" for key, value in kwargs.items()])
        print(f"Метод {func.__name__} вызван в {timestamp} с аргументами: {arguments}")
        return result

    return wrapper
task_list = TaskList()

@log_activity
def add_task(task_list, title, description):
    task_list.create_task(title, description)

@log_activity
def complete_task(task_list, index):
    task = task_list.get_task(index)
    if task:
        task.mark_as_done()

@log_activity
def edit_task_description(task_list, index, new_description):
    task = task_list.get_task(index)
    if task:
        task.edit_description(new_description)

@log_activity
def remove_task(task_list, index):
    task_list.remove_task(index)

add_task(task_list, "написать код", "осознать что без помощи гугла и боженьки не справиться")
add_task(task_list, "взять себя в руки", "напрячь все свои извилины и создать код ,пересиливая в себе навязчивое желание вставить код из Chat GPT")
# complete_task(task_list, 0)
# edit_task_description(task_list, 2, "погуглив проанализировав информацию написать код")
# remove_task(task_list, 2)

# for task in task_list.get_all_tasks():
#     print(task)

# import json

# # ...

# def save_task_list(task_list, filename):
#     tasks = [task.__dict__ for task in task_list.get_all_tasks()]
#     with open(filename, 'w') as file:
#         json.dump(tasks, file, indent=4)

# save_task_list(task_list, 'task_list.json')



# def load_task_list(filename):
#     with open(filename, 'r') as file:
#         tasks_data = json.load(file)
    
#     task_list = TaskList()
#     for task_data in tasks_data:
#         title = task_data['title']
#         description = task_data['description']
        
#         task = Task(title, description)
#         task.status = task_data['status']
#         task.creation_date = datetime.datetime.strptime(task_data['creation_date'], "%Y-%m-%d %H:%M:%S")
        
#         task_list.create_task(task)
    
#     return task_list

# task_list = load_task_list('task_list.json'
