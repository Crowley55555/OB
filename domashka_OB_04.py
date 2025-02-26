# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
# Исходные данные:
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
# Шаг 3: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from abc import ABC, abstractmethod  # Импортируем модуль для работы с абстрактными классами

# *** Класс Fighter представляет бойца, который может использовать разное оружие для атаки монстра.
class Fighter:
    def __init__(self, name):
        """
        *** Конструктор класса Fighter.
        :param name: Имя бойца.
        """
        self.weapon = None  # Текущее оружие бойца
        self.name = name  # Имя бойца

    def change_weapon(self, weapon):
        """
        *** Метод для изменения оружия бойца.
        :param weapon: Объект оружия, которое будет использоваться бойцом.
        """
        self.weapon = weapon
        print(f"{self.name} выбрал {self.weapon.__class__.__name__}")  # Выводим сообщение о смене оружия

    def attack(self, monster):
        """
        *** Метод для атаки монстра.
        :param monster: Объект монстра, который подвергается атаке.
        """
        if self.weapon is not None:  # Проверяем, есть ли у бойца оружие
            self.weapon.attack(self.name, monster)  # Вызываем метод атаки оружия
        else:
            print(f"{self.name} не выбрал оружие")  # Если оружия нет, выводим сообщение об ошибке

# *** Класс Monster представляет монстра, который имеет здоровье и может получать урон.
class Monster:
    def __init__(self, healh):
        """
        *** Конструктор класса Monster.
        :param healh: Начальное здоровье монстра.
        """
        self.health = healh  # Здоровье монстра

    def take_damage(self, damage):
        """
        *** Метод для применения урона к здоровью монстра.
        :param damage: Количество урона, которое получает монстр.
        """
        self.health -= damage  # Уменьшаем здоровье монстра на величину урона
        if self.health <= 0:  # Проверяем, повержен ли монстр
            print("Монстр побежден!")
        else:
            print(f"Монстр остался с {self.health} здоровья")  # Выводим текущее здоровье монстра

# *** Абстрактный класс Weapon определяет интерфейс для всех типов оружия.
class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter_name, monster):
        """
        *** Абстрактный метод для выполнения атаки.
        :param fighter_name: Имя бойца, который атакует.
        :param monster: Объект монстра, который получает урон.
        """
        pass

# *** Класс Sword представляет меч как тип оружия.
class Sword(Weapon):
    def attack(self, fighter_name, monster):
        """
        *** Метод для атаки мечом.
        :param fighter_name: Имя бойца, который атакует.
        :param monster: Объект монстра, который получает урон.
        """
        damage = 30  # Урон от меча
        print(f"{fighter_name} атаковал мечом, нанес {damage} урона")  # Выводим сообщение об атаке
        monster.take_damage(damage)  # Применяем урон к монстру

# *** Класс Bow представляет лук как тип оружия.
class Bow(Weapon):
    def attack(self, fighter_name, monster):
        """
        *** Метод для атаки луком.
        :param fighter_name: Имя бойца, который атакует.
        :param monster: Объект монстра, который получает урон.
        """
        damage = 30  # Урон от лука
        print(f"{fighter_name} атаковал Луком, нанес {damage} урона")  # Выводим сообщение об атаке
        monster.take_damage(damage)  # Применяем урон к монстру

# *** Класс Spear представляет копье как тип оружия.
class Spear(Weapon):
    def attack(self, fighter_name, monster):
        """
        *** Метод для атаки копьем.
        :param fighter_name: Имя бойца, который атакует.
        :param monster: Объект монстра, который получает урон.
        """
        damage = 40  # Урон от копья
        print(f"{fighter_name} атаковал копьем, нанес {damage} урона")  # Выводим сообщение об атаке
        monster.take_damage(damage)  # Применяем урон к монстру

# *** Точка входа в программу. Здесь происходит тестирование функциональности.
if __name__ == "__main__":
    name = "Вася"  # Имя бойца
    monster_health = 100  # Начальное здоровье монстра

    fighter = Fighter(name)  # Создаем объект бойца
    monster = Monster(monster_health)  # Создаем объект монстра

    fighter.change_weapon(Sword())  # Боец выбирает меч
    fighter.attack(monster)  # Боец атакует монстра мечом

    fighter.change_weapon(Bow())  # Боец меняет оружие на лук
    fighter.attack(monster)  # Боец атакует монстра луком

    fighter.change_weapon(Spear())  # Боец меняет оружие на копье
    fighter.attack(monster)  # Боец атакует монстра копьем