class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__user_list = []

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Invalid user type.")

    def remove_user(self, user_id):
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                self.__user_list.remove(user)
                print(f"User ID {user_id} removed.")
                return
        print(f"User ID {user_id} not found.")

    def list_users(self):
        return [(user.get_user_id(), user.get_name()) for user in self.__user_list]


# Создание администратора и пользователей
admin = Admin(1, "Admin John")
user1 = User(2, "Alice")
user2 = User(3, "Bob")

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)
print(f"Пользователей после добавления: {len(admin.list_users())}")  # 2

# Администратор удаляет пользователя
admin.remove_user(user1.get_user_id())
print(f"Пользователей после удаления: {len(admin.list_users())}")    # 1

# Проверка уровня доступа
print(f"Уровень доступа администратора: {admin.get_access_level()}")  # admin