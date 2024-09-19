from datetime import datetime


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Задача с таким индексом не найдена!")

    def show_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if incomplete_tasks:
            print("Текущие задачи:")
            for i, task in enumerate(incomplete_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Все задачи выполнены!")

    def show_all_tasks(self):
        if self.tasks:
            print("Все задачи:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Список задач пуст!")


class TaskManagerInterface:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Добавить задачу")
            print("2. Отметить задачу как выполненную")
            print("3. Показать текущие задачи")
            print("4. Показать все задачи")
            print("5. Выйти")

            choice = input("Выберите действие (1-5): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.complete_task()
            elif choice == "3":
                self.manager.show_incomplete_tasks()
            elif choice == "4":
                self.manager.show_all_tasks()
            elif choice == "5":
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")

    def add_task(self):
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи (в формате ГГГГ-ММ-ДД): ")

        # Простой способ проверки валидности даты
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Неверный формат даты! Задача не добавлена.")
            return

        self.manager.add_task(description, deadline)
        print("Задача добавлена!")

    def complete_task(self):
        try:
            task_index = int(input("Введите номер задачи, которую хотите отметить выполненной: ")) - 1
            self.manager.complete_task(task_index)
            print("Задача выполнена!")
        except ValueError:
            print("Неверный ввод! Введите числовой индекс.")


# Запуск программы
interface = TaskManagerInterface()
interface.run()
