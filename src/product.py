from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для создания товаров"""

    name: str
    description: str
    price: float
    quantity: int

    # Создаем конструктор класса, который принимает данные для создания объекта
    def __init__(self, name, description, price, quantity):  # Конструктор
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут цены
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, product_data):
        """Принимает на вход параметры товара в словаре и возвращает созданный объект класса Product."""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        return cls(name, description, price, quantity)

    def __str__(self):
        """Выводит строковое отображение в определённом виде"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает сумму произведений цены на количество у двух объектов"""
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @property
    def price(self):
        """Геттер выводит цену товара"""
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
