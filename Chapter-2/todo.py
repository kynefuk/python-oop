class Todo(object):

    last_id = 0

    def __init__(self, title, due_time, tags):
        self.title = title
        self.due_time = due_time
        self.tags = tags
        Todo.last_id += 1
        self.id = Todo.last_id

    def match(self, filter):
        return filter in self.title or filter in self.tags


class Manager(object):
    def __init__(self, *args, **kwargs):
        self.todo_list = []

    def add_todo(self, title=None, due_time=None, tags=None):
        self.todo_list.append(Todo(title, due_time, tags))

    def _find_todo(self, todo_id):
        for todo in self.todo_list:
            if str(todo_id) == str(todo.id):
                return todo
                break

        raise Exception("id is not valid")

    def modify_title(self, todo_id, title):
        todo = self._find_todo(todo_id)
        todo.title = title

    def modify_due_time(self, todo_id, due_time):
        todo = self._find_todo(todo_id)
        todo.due_time = due_time

    def modify_tags(self, todo_id, tags):
        todo = self._find_todo(todo_id)
        todo.tags = tags

    def delete_todo(self, todo_id):
        todo = self._find_todo(todo_id)
        self.todo_list.remove(todo)

    def search_todo(self, filter):
        [todo for todo in self.todo_list if todo.match(filter)]
