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

    def middle_price(self):
        try:
            return sum([price.price for price in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        """Геттер, который будет выводить список товаров в виде строк"""
        return ". ".join(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products)

if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
