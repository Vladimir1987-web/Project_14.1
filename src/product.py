class Product:
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
