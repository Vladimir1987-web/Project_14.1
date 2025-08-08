import pytest


def test_product_init(products_1):
    assert products_1.name == "Samsung Galaxy S23 Ultra"
    assert products_1.description == "256GB, Серый цвет, 200MP камера"
    assert products_1.price == 180000.0
    assert products_1.quantity == 5
