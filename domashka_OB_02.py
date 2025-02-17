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

    def set_access_level(self, access_level):
        self.__access_level = access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__user_list = []

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        if isinstance(user, User):
            if any(u.get_user_id() == user.get_user_id() for u in self.__user_list):
                print(f"User ID {user.get_user_id()} already exists.")
                return
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

    def find_user_by_id(self, user_id):
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                return user
        return None

    def find_user_by_name(self, name):
        for user in self.__user_list:
            if user.get_name() == name:
                return user
        return None

    def change_user_name(self, user_id, new_name):
        user = self.find_user_by_id(user_id)
        if user:
            user.set_name(new_name)
            print(f"User ID {user_id} name changed to {new_name}.")
        else:
            print(f"User ID {user_id} not found.")

    def change_user_access_level(self, user_id, new_access_level):
        user = self.find_user_by_id(user_id)
        if user:
            user.set_access_level(new_access_level)
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

print(f"Пользователей после добавления: {len(admin.list_users())}")  # 2

admin.change_user_name(2, "Alice Smith")
admin.change_user_access_level(3, 'admin')

print(f"Имя пользователя 2: {admin.find_user_by_id(2).get_name()}")  # Alice Smith
print(f"Имя пользователя 3: {admin.find_user_by_id(3).get_name()}")
print(f"Имя пользователя 3: {admin.find_user_by_id(4).get_name()}")
print(f"Уровень доступа пользователя 3: {admin.find_user_by_id(3).get_access_level()}")  # admin
print(f"Уровень доступа пользователя 4: {admin.find_user_by_id(5).get_access_level()}")

admin.remove_user(2)
admin.remove_user(3)
print(f"Пользователей после удаления: {len(admin.list_users())}")  # 1
