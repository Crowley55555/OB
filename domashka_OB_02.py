class User:
    """
    Класс User представляет пользователя в системе.

    Атрибуты:
        user_id (int): Уникальный идентификатор пользователя.
        name (str): Имя пользователя.
        access_level (str): Уровень доступа пользователя.

    Методы:
        get_user_id(): Возвращает идентификатор пользователя.
        get_name(): Возвращает имя пользователя.
        get_access_level(): Возвращает уровень доступа пользователя.
        set_name(name): Устанавливает новое имя пользователя.
        set_access_level(access_level): Устанавливает новый уровень доступа пользователя.
    """

    def __init__(self, user_id, name):
        """Инициализирует новый экземпляр класса User."""
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        """Возвращает уникальный идентификатор пользователя."""
        return self.__user_id

    def get_name(self):
        """Возвращает имя пользователя."""
        return self.__name

    def get_access_level(self):
        """Возвращает уровень доступа пользователя."""
        return self.__access_level

    def set_name(self, name):
        """Устанавливает новое имя пользователя."""
        self.__name = name

    def set_access_level(self, access_level):
        """Устанавливает новый уровень доступа пользователя."""
        self.__access_level = access_level


class Admin(User):
    """
    Класс Admin представляет администратора в системе. Наследует от класса User.

    Атрибуты:
        user_list (list): Список пользователей, которыми управляет администратор.

    Методы:
        add_user(user): Добавляет пользователя в список.
        remove_user(user_id): Удаляет пользователя из списка по ID.
        list_users(): Возвращает список всех пользователей.
        find_user_by_id(user_id): Находит пользователя по ID.
        find_user_by_name(name): Находит пользователя по имени.
        change_user_name(user_id, new_name): Изменяет имя пользователя.
        change_user_access_level(user_id, new_access_level): Изменяет уровень доступа пользователя.
    """

    def __init__(self, user_id, name):
        """Инициализирует новый экземпляр класса Admin."""
        super().__init__(user_id, name)
        self.set_access_level('admin')  # Устанавливаем уровень доступа администратора
        self.__user_list = []

    def add_user(self, user):
        """
        Добавляет пользователя в список.

        Аргументы:
            user (User): Экземпляр класса User.
        """
        if isinstance(user, User):
            # Проверка на дублирование ID
            if any(u.get_user_id() == user.get_user_id() for u in self.__user_list):
                print(f"User ID {user.get_user_id()} already exists.")
                return
            self.__user_list.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Invalid user type.")

    def remove_user(self, user_id):
        """
        Удаляет пользователя из списка по ID.

        Аргументы:
            user_id (int): Уникальный идентификатор пользователя.
        """
        target_user = self.find_user_by_id(user_id)
        if target_user:
            self.__user_list.remove(target_user)
            print(f"User ID {user_id} removed.")
        else:
            print(f"User ID {user_id} not found.")  # Исправлено: предложение начинается с заглавной буквы.

    def list_users(self):
        """Возвращает список всех пользователей."""
        return [(user.get_user_id(), user.get_name()) for user in self.__user_list]

    def find_user_by_id(self, user_id):
        """
        Находит пользователя по ID.

        Аргументы:
            user_id (int): Уникальный идентификатор пользователя.

        Возвращает:
            User: Экземпляр класса User, если найден, иначе None.
        """
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                return user
        return None

    def find_user_by_name(self, name):
        """
        Находит пользователя по имени.

        Аргументы:
            name (str): Имя пользователя.

        Возвращает:
            User: Экземпляр класса User, если найден, иначе None.
        """
        for user in self.__user_list:
            if user.get_name() == name:
                return user
        return None

    def change_user_name(self, user_id, new_name):
        """
        Изменяет имя пользователя.

        Аргументы:
            user_id (int): Уникальный идентификатор пользователя
            new_name (str): Новое имя пользователя.
        """
        target_user = self.find_user_by_id(user_id)
        if target_user:
            target_user.set_name(new_name)
            print(f"User ID {user_id} name changed to {new_name}.")
        else:
            print(f"User ID {user_id} not found.")  # Исправлено: предложение начинается с заглавной буквы.

    def change_user_access_level(self, user_id, new_access_level):
        """
        Изменяет уровень доступа пользователя.

        Аргументы:
        user_id (int): Уникальный идентификатор пользователя
        new_access_level (str): Новый уровень доступа пользователя.
        """
        target_user = self.find_user_by_id(user_id)
        if target_user:
            target_user.set_access_level(new_access_level)
            print(f"User ID {user_id} access level changed to {new_access_level}.")
        else:
            print(f"User ID {user_id} not found.")


# Пример использования
admin = Admin(1, "Admin John")
user1 = User(2, "Alice")
user2 = User(3, "Вася")
user3 = User(4, "Петя")
user4 = User(5, "Маша")
user5 = User(6, "Валера")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)
admin.add_user(user5)

print(f"Пользователей после добавления: {len(admin.list_users())}")  # 5

admin.change_user_name(2, "Alice Smith")
admin.change_user_access_level(3, 'admin')

# Проверка наличия пользователя перед вызовом метода get_name
found_user = admin.find_user_by_id(2)
if found_user:
    print(f"Имя пользователя 2: {found_user.get_name()}")  # Alice Smith
else:
    print("Пользователь не найден.")

found_user = admin.find_user_by_id(3)
if found_user:
    print(f"Имя пользователя 3: {found_user.get_name()}")  # Вася
else:
    print("Пользователь не найден.")

found_user = admin.find_user_by_id(4)
if found_user:
    print(f"Имя пользователя 4: {found_user.get_name()}")  # Петя
else:
    print("Пользователь не найден.")

found_user = admin.find_user_by_id(3)
if found_user:
    print(f"Уровень доступа пользователя 3: {found_user.get_access_level()}")  # admin
else:
    print("Пользователь не найден.")

found_user = admin.find_user_by_id(5)
if found_user:
    print(f"Уровень доступа пользователя 5: {found_user.get_access_level()}")  # user
else:
    print("Пользователь не найден.")

admin.remove_user(2)
admin.remove_user(3)
print(f"Пользователей после удаления: {len(admin.list_users())}")  # 3