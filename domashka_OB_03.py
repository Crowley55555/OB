import json
import logging
from abc import ABC, abstractmethod
import pandas as pd

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
        """Выводит список животных."""
        print("Вот список животных:")
        for animal in self.animals:
            print(animal)

    def show_employees(self):
        """Выводит список сотрудников."""
        print("Вот список сотрудников:")
        for employee in self.employees:
            print(employee)

    def save_to_file(self, filename):
        """Сохраняет данные зоопарка в JSON-файл."""
        data = {
            "animals": [animal.to_dict() for animal in self.animals],
            "employees": [{"name": emp.name, "type": emp.__class__.__name__} for emp in self.employees]
        }
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            logging.info(f"Данные сохранены в файл {filename}")
        except IOError as e:
            logging.error(f"Ошибка при сохранении файла: {e}")

    def load_from_file(self, filename):
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

    def save_to_excel(self, filename):
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

def main():
    zoo = Zoo()

    while True:
        print("\nМеню:")
        print("1. Добавить животное")
        print("2. Добавить сотрудника")
        print("3. Показать список животных")
        print("4. Показать список сотрудников")
        print("5. Сохранить данные в JSON")
        print("6. Сохранить данные в Excel")
        print("7. Загрузить данные из JSON")
        print("8. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            animal_type = input("Введите тип животного (Bird, Mammal, Reptile, Fish): ").strip()
            name = input("Введите имя животного: ").strip()
            age = int(input("Введите возраст животного: ").strip())
            try:
                if animal_type == "Bird":
                    zoo.add_animal(Bird(name, age))
                elif animal_type == "Mammal":
                    zoo.add_animal(Mammal(name, age))
                elif animal_type == "Reptile":
                    zoo.add_animal(Reptile(name, age))
                elif animal_type == "Fish":
                    zoo.add_animal(Fish(name, age))
                else:
                    print("Неизвестный тип животного.")
            except AnimalValidationError as e:
                logging.error(f"Ошибка при добавлении животного: {e}")

        elif choice == "2":
            employee_type = input("Введите тип сотрудника (ZooKeeper, Veterinarian): ").strip()
            name = input("Введите имя сотрудника: ").strip()
            if employee_type == "ZooKeeper":
                zoo.add_employee(ZooKeeper(name))
            elif employee_type == "Veterinarian":
                zoo.add_employee(Veterinarian(name))
            else:
                print("Неизвестный тип сотрудника.")

        elif choice == "3":
            zoo.show_animals()

        elif choice == "4":
            zoo.show_employees()

        elif choice == "5":
            filename = input("Введите имя файла для сохранения в JSON: ").strip()
            zoo.save_to_file(filename)

        elif choice == "6":
            filename = input("Введите имя файла для сохранения в Excel: ").strip()
            zoo.save_to_excel(filename)

        elif choice == "7":
            filename = input("Введите имя файла для загрузки из JSON: ").strip()
            try:
                zoo.load_from_file(filename)
            except (ZooFileNotFoundError, InvalidZooDataError) as e:
                logging.error(f"Ошибка при загрузке данных: {e}")

        elif choice == "8":
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
