class Product:
    name: str
    description: str
    price: float
    quantity: int

    # Создаем конструктор класса, который принимает данные для создания объекта
    def __init__(self, name, description, price, quantity):  # Конструктор
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
