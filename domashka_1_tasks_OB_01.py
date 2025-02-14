class Task:
    def __init__(self, description: str, deadline: str):
        self.description = description
        self.deadline = deadline
        self.status = False

    def __str__(self):
        return f"Описание: {self.description}, Срок: {self.deadline}, Статус: {'✅ Выполнено' if self.status else '❌ Не выполнено'}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str, deadline: str) -> None:
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_completed(self, task_index: int) -> None:
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].status = True
        else:
            raise IndexError("Неверный индекс задачи")

    def get_current_tasks(self) -> list:
        return [task for task in self.tasks if not task.status]

    def display_current_tasks(self) -> None:
        current_tasks = self.get_current_tasks()
        if not current_tasks:
            print("\n--- Нет активных задач ---")
            return

        print("\n=== ТЕКУЩИЕ ЗАДАЧИ ===")
        for idx, task in enumerate(current_tasks, 1):
            print(f"{idx}. {task}")

def main():
    manager = TaskManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать текущие задачи")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения задачи: ")
            manager.add_task(description, deadline)
            print("Задача добавлена!")

        elif choice == '2':
            manager.display_current_tasks()
            task_index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
            try:
                manager.mark_completed(task_index)
                print("Статус задачи обновлен!")
            except IndexError as e:
                print(e)

        elif choice == '3':
            manager.display_current_tasks()

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()