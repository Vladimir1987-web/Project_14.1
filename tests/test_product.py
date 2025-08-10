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
