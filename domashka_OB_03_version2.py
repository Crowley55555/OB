import json
import logging
from abc import ABC, abstractmethod
import pandas as pd
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from typing import TextIO

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Пользовательские исключения
class ZooFileNotFoundError(Exception):
    """Исключение, если файл с данными зоопарка не найден."""
    pass

class InvalidZooDataError(Exception):
    """Исключение, если данные в файле повреждены."""
    pass

class AnimalValidationError(Exception):
    """Исключение, если данные животного невалидны."""
    pass

# Базовый класс Animal
class Animal(ABC):
    """Базовый класс для всех животных."""
    def __init__(self, name, age):
        """Инициализирует животное с именем и возрастом."""
        if not name:
            raise AnimalValidationError("Имя не может быть пустым")
        if age < 0:
            raise AnimalValidationError("Возраст не может быть отрицательным")
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        """Издаёт звук, характерный для животного."""
        pass

    @abstractmethod
    def eat(self):
        """Описание процесса питания."""
        pass

    def to_dict(self):
        """Преобразует объект животного в словарь для сериализации."""
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data):
        """Создаёт объект животного из словаря."""
        if data["type"] == "Bird":
            return Bird(data["name"], data["age"])
        elif data["type"] == "Mammal":
            return Mammal(data["name"], data["age"])
        elif data["type"] == "Reptile":
            return Reptile(data["name"], data["age"])
        elif data["type"] == "Fish":
            return Fish(data["name"], data["age"])
        else:
            raise InvalidZooDataError(f"Неизвестный тип животного: {data['type']}")

    def __str__(self):
        """Строковое представление животного."""
        return f"{self.__class__.__name__}: {self.name}, возраст: {self.age}"

# Классы животных
class Bird(Animal):
    """Класс, представляющий птиц."""
    def make_sound(self):
        print("Чик чирик")

    def eat(self):
        print("зерно")

class Mammal(Animal):
    """Класс, представляющий млекопитающих."""
    def make_sound(self):
        print("мяу")

    def eat(self):
        print("мясо")

class Reptile(Animal):
    """Класс, представляющий рептилий."""
    def make_sound(self):
        print("шум")

    def eat(self):
        print("все подряд")

class Fish(Animal):
    """Класс, представляющий рыб."""
    def make_sound(self):
        print("Буль-буль")

    def eat(self):
        print("планктон")

# Класс Zoo
class Zoo:
    """Класс, представляющий зоопарк."""
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal: Animal):
        """Добавляет животное в зоопарк."""
        self.animals.append(animal)
        logging.info(f"Добавлено новое животное: {animal}")

    def add_employee(self, employee):
        """Добавляет сотрудника в зоопарк."""
        self.employees.append(employee)
        logging.info(f"Добавлен новый сотрудник: {employee}")

    def get_animals(self):
        """Возвращает список животных."""
        return self.animals

    def get_employees(self):
        """Возвращает список сотрудников."""
        return self.employees

    def show_animals(self):
        """Возвращает строковое представление списка животных."""
        return "\n".join(str(animal) for animal in self.animals)

    def show_employees(self):
        """Возвращает строковое представление списка сотрудников."""
        return "\n".join(str(employee) for employee in self.employees)

    def save_to_file(self, filename: str):
        """Сохраняет данные зоопарка в JSON-файл."""
        data = {
            "animals": [animal.to_dict() for animal in self.animals],
            "employees": [{"name": emp.name, "type": emp.__class__.__name__} for emp in self.employees]
        }
        file: TextIO
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        logging.info(f"Данные сохранены в файл {filename}")

    def load_from_file(self, filename: str):
        """Загружает данные зоопарка из JSON-файла."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            raise ZooFileNotFoundError(f"Файл {filename} не найден")
        except json.JSONDecodeError:
            raise InvalidZooDataError(f"Данные в файле {filename} повреждены")

        self.animals = [Animal.from_dict(animal_data) for animal_data in data["animals"]]
        self.employees = []
        for emp_data in data["employees"]:
            if emp_data["type"] == "ZooKeeper":
                self.employees.append(ZooKeeper(emp_data["name"]))
            elif emp_data["type"] == "Veterinarian":
                self.employees.append(Veterinarian(emp_data["name"]))
        logging.info(f"Данные загружены из файла {filename}")

    def save_to_excel(self, filename: str):
        """Сохраняет данные о животных в Excel-файл."""
        data = {
            "type": [animal.__class__.__name__ for animal in self.animals],
            "name": [animal.name for animal in self.animals],
            "age": [animal.age for animal in self.animals]
        }
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        logging.info(f"Данные о животных сохранены в Excel-файл {filename}")

# Классы сотрудников
class ZooKeeper:
    """Класс, представляющий смотрителя зоопарка."""
    def __init__(self, name):
        self.name = name

    def feed_animal(self):
        """Кормит животное."""
        print(f"{self.name} кормит животное")

    def clean_enclosure(self):
        """Убирает вольер."""
        print(f"{self.name} убирает вольер")

    def __str__(self):
        return f"Смотритель зоопарка: {self.name}"

class Veterinarian:
    """Класс, представляющий ветеринара."""
    def __init__(self, name):
        self.name = name

    def heal_animal(self):
        """Лечит животное."""
        print(f"{self.name} лечит животное")

    def check_health(self, animal):
        """Проверяет здоровье животного."""
        print(f"{self.name} проверяет здоровье {animal.name}")

    def __str__(self):
        return f"Ветеринар: {self.name}"

class ZooApp:
    """Класс для графического интерфейса приложения зоопарка."""
    def __init__(self, window):
        self.window = window
        self.window.title("Зоопарк")
        self.zoo = Zoo()

        self.add_animal_button = None
        self.add_employee_button = None
        self.show_animals_button = None
        self.show_employees_button = None
        self.save_json_button = None
        self.save_excel_button = None
        self.load_json_button = None

        self.create_widgets()

    def create_widgets(self):
        """Создает виджеты интерфейса."""
        self.add_animal_button = tk.Button(self.window, text="Добавить животное", command=self.add_animal)
        self.add_animal_button.pack(pady=5)

        self.add_employee_button = tk.Button(self.window, text="Добавить сотрудника", command=self.add_employee)
        self.add_employee_button.pack(pady=5)

        self.show_animals_button = tk.Button(self.window, text="Показать животных", command=self.show_animals)
        self.show_animals_button.pack(pady=5)

        self.show_employees_button = tk.Button(self.window, text="Показать сотрудников", command=self.show_employees)
        self.show_employees_button.pack(pady=5)

        self.save_json_button = tk.Button(self.window, text="Сохранить в JSON", command=self.save_to_json)
        self.save_json_button.pack(pady=5)

        self.save_excel_button = tk.Button(self.window, text="Сохранить в Excel", command=self.save_to_excel)
        self.save_excel_button.pack(pady=5)

        self.load_json_button = tk.Button(self.window, text="Загрузить из JSON", command=self.load_from_json)
        self.load_json_button.pack(pady=5)

    def add_animal(self):
        """Добавляет животное в зоопарк."""
        animal_type = simpledialog.askstring("Тип животного", "Введите тип животного (Bird, Mammal, Reptile, Fish):")
        name = simpledialog.askstring("Имя животного", "Введите имя животного:")
        age = simpledialog.askinteger("Возраст животного", "Введите возраст животного:")
        try:
            if animal_type == "Bird":
                self.zoo.add_animal(Bird(name, age))
            elif animal_type == "Mammal":
                self.zoo.add_animal(Mammal(name, age))
            elif animal_type == "Reptile":
                self.zoo.add_animal(Reptile(name, age))
            elif animal_type == "Fish":
                self.zoo.add_animal(Fish(name, age))
            else:
                messagebox.showerror("Ошибка", "Неизвестный тип животного.")
        except AnimalValidationError as e:
            messagebox.showerror("Ошибка", f"Ошибка при добавлении животного: {e}")

    def add_employee(self):
        """Добавляет сотрудника в зоопарк."""
        employee_type = simpledialog.askstring("Тип сотрудника", "Введите тип сотрудника (ZooKeeper, Veterinarian):")
        name = simpledialog.askstring("Имя сотрудника", "Введите имя сотрудника:")
        if employee_type == "ZooKeeper":
            self.zoo.add_employee(ZooKeeper(name))
        elif employee_type == "Veterinarian":
            self.zoo.add_employee(Veterinarian(name))
        else:
            messagebox.showerror("Ошибка", "Неизвестный тип сотрудника.")

    def show_animals(self):
        """Показывает список животных."""
        animals_list = self.zoo.show_animals()
        messagebox.showinfo("Животные", animals_list)

    def show_employees(self):
        """Показывает список сотрудников."""
        employees_list = self.zoo.show_employees()
        messagebox.showinfo("Сотрудники", employees_list)

    def save_to_json(self):
        """Сохраняет данные в JSON-файл."""
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            self.zoo.save_to_file(filename)

    def save_to_excel(self):
        """Сохраняет данные в Excel-файл."""
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if filename:
            self.zoo.save_to_excel(filename)

    def load_from_json(self):
        """Загружает данные из JSON-файла."""
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            try:
                self.zoo.load_from_file(filename)
                messagebox.showinfo("Успех", "Данные успешно загружены.")
            except (ZooFileNotFoundError, InvalidZooDataError) as e:
                messagebox.showerror("Ошибка", f"Ошибка при загрузке данных: {e}")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = ZooApp(main_window)
    main_window.mainloop()
