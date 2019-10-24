import os
import sys

from notebook import Manager


class Menu(object):
    linesep = os.linesep

    def __init__(self, *args, **kwargs):
        self.manager = Manager()
        self.choices = {
            "1": self.show_todos,
            "2": self.add_todo,
            "3": self.modify_todo_title,
            "4": self.modify_todo_due_time,
            "5": self.modify_todo_tags,
            "6": self.delete_todo,
            "7": self.quit,
        }

    def display(self):
        print(
            """
        1. Show Todos
        2. Add Todo
        3. Modify Todo's Title
        4. Modify Todo's Due Time
        5. Modify Todo's tags
        6. Delete Todo
        7. Quit
        """
        )

    def run(self):
        while True:
            self.display()
            choice = input("Enter option:")

            action = self.choices.get(choice)

            if action:
                try:
                    action()
                except Exception as e:
                    print(e)
                    pass
            else:
                print("your option {choice} is not valid")

    def show_todos(self, manager=None):

        if not manager:
            manager = Manager()

        for todo in self.manager.todo_list:
            title = todo.title
            due_time = todo.due_time
            tags = todo.tags
            id = todo.id

            print(
                f"Title:{title}{Menu.linesep}Due_Time:{due_time}{Menu.linesep}Tags:{tags}{Menu.linesep}ID:{id}"
            )

    def add_todo(self):
        title = input("Enter Todo's title:")
        due_time = input("Enter Todo's due_time:")
        tags = input("Enter Todo's tags:")
        self.manager.add_todo(title, due_time, tags)

        print("New Todo has been created")

    def modify_todo_title(self):
        todo_id = input("Enter Todo's id:")
        title = input("Enter new Todo's title:")
        self.manager.modify_title(todo_id, title)

        print("Todo has been updated!")

    def modify_todo_due_time(self):
        todo_id = input("Enter Todo's id:")
        due_time = input("Enter new Todo's due_time:")
        self.manager.modify_due_time(todo_id, due_time)

        print("Todo has been updated!")

    def modify_todo_tags(self):
        todo_id = input("Enter Todo's id:")
        tags = input("Enter new Todo's tags:")
        self.manager.modify_tags(todo_id, tags)

        print("Todo has been updated!")

    def delete_todo(self):
        todo_id = input("Enter Todo's id:")
        self.manager.delete_todo(todo_id)

        print("Todo has been deleted!")

    def quit(self):
        print("Thank you!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
