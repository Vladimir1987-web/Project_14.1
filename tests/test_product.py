import pytest


def test_product_init(products_1):
    assert products_1.name == "Samsung Galaxy S23 Ultra"
    assert products_1.description == "256GB, Серый цвет, 200MP камера"
    assert products_1.price == 180000.0
    assert products_1.quantity == 5


def test_product_method(new_product):
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_product_price_empy(new_product):
    new_product.price = 0
    assert new_product.price == 180000.0
    new_product.price = 800
    assert new_product.price == 800
    new_product.price = -100
    assert new_product.price == 800


def test_product_price_error_message(new_product, capfd):
    new_product.price = 0
    captured = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_str(products_1):
    assert str(products_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(products_1, products_2):
    assert products_1 + products_2 == 2580000.0


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_lawngrass_init(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_product_add_error(smartphone1, grass1):
    with pytest.raises(TypeError):
        invalid_sum = smartphone1 + grass1
