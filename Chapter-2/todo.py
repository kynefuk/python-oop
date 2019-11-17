class Todo(object):
    """
    Todoクラス
    """

    last_id = 0

    def __init__(self, title, due_time, tags):
        Todo.last_id += 1
        self.title = title
        self.due_time = due_time
        self.tags = tags
        self.id = Todo.last_id

    def match(self, filter):
        """
        引数がタイトルかタグにマッチするか判定
        """

        return filter in self.title or filter in self.tags


class Manager(object):
    """
    Todo管理を行うマネージャクラス
    """

    def __init__(self, *args, **kwargs):
        self.todo_list = []

    def add_todo(self, title=None, due_time=None, tags=None):
        """
        Todoをリストに追加する
        """

        self.todo_list.append(Todo(title, due_time, tags))

    def _find_todo(self, todo_id):
        """
        合致するIDのTodoを返却する
        マネージャクラス内部で使用する
        """

        for todo in self.todo_list:
            if str(todo_id) == str(todo.id):
                return todo
                break

        raise Exception("id is not valid")

    def modify_title(self, todo_id, title):
        """
        Todoのタイトルの編集を行う
        """

        todo = self._find_todo(todo_id)
        todo.title = title

    def modify_due_time(self, todo_id, due_time):
        """
        Todoの期限の編集を行う
        """

        todo = self._find_todo(todo_id)
        todo.due_time = due_time

    def modify_tags(self, todo_id, tags):
        """
        Todoのタグの編集を行う
        """

        todo = self._find_todo(todo_id)
        todo.tags = tags

    def delete_todo(self, todo_id):
        """
        Todoの削除を行う
        """

        todo = self._find_todo(todo_id)
        self.todo_list.remove(todo)
