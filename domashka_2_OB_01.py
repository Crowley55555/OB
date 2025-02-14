class Store:
    def __init__(self, name, address):
        """Инициализация магазина с названием, адресом и пустым словарем товаров."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаление товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получение цены товара по его названию. Возвращает None, если товар отсутствует."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновление цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание первого магазина
store1 = Store("Green Grocery", "123 Main St")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store1.add_item("oranges", 0.8)

# Создание второго магазина
store2 = Store("Fresh Market", "456 Elm St")
store2.add_item("milk", 1.2)
store2.add_item("bread", 2.0)
store2.add_item("eggs", 1.5)

# Создание третьего магазина
store3 = Store("Organic Foods", "789 Oak St")
store3.add_item("carrots", 0.6)
store3.add_item("lettuce", 1.1)
store3.add_item("tomatoes", 1.3)

# Примеры использования методов
print(store1.get_price("apples"))  # Вывод: 0.5
store1.update_price("apples", 0.55)
print(store1.get_price("apples"))  # Вывод: 0.55
store1.remove_item("oranges")
print(store1.get_price("oranges"))  # Вывод: None