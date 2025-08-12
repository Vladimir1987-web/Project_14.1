class Product:
    """Класс для создания товаров"""

    name: str
    description: str
    price: float
    quantity: int

    # Создаем конструктор класса, который принимает данные для создания объекта
    def __init__(self, name, description, price, quantity):  # Конструктор
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает сумму произведений цены на количество у двух объектов"""
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        """Сеттер для цены продукта с проверкой."""
        if int(price) <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
