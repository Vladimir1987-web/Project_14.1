from src.product import LawnGrass, Product, Smartphone


class Category:
    """Класс для категорий товаров"""

    # Атрибуты класса
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация объектов класса"""
        self.name = name
        self.description = description
        self.__products = products  # приватный атрибут списка продуктов
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Выводит строковое отображение в определённом виде"""
        quantity_prod = 0
        for prod in self.__products:
            quantity_prod += prod.quantity

        return f"{self.name}, количество продуктов: {quantity_prod} шт."

    def add_product(self, product: Product):
        """Специальный метод для добавления товаров в категорию.
        Записывает объект класса Product в приватный атрибут списка товаров."""
        if isinstance(product, Smartphone) or isinstance(product, LawnGrass) or isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер, который будет выводить список товаров в виде строк"""
        return ". ".join(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products)
