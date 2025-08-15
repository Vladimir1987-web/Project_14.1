import pytest

from src.category import Category
from src.product import Product

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category1():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )


def test_category_init(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert (
        category1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.. Iphone 15, 210000.0 "
        "руб. Остаток: 8 шт."
    )
    assert category1.category_count == 1
    assert category1.product_count == 2


def test_category_add_product(category1):
    category1.add_product(product4)
    assert category1.product_count == 5
    assert (
        category1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.. Iphone 15,"
        ' 210000.0 руб. Остаток: 8 шт.. 55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
    )


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_category_add_product_error(category1):
    with pytest.raises(TypeError):
        category1.add_product("Not a product")
