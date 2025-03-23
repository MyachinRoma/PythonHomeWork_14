import pytest


def test_smartphone_init(product_Smartphone1):
    assert product_Smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_Smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert product_Smartphone1.price == 180000
    assert product_Smartphone1.quantity == 5
    assert product_Smartphone1.efficiency == 95.5
    assert product_Smartphone1.model == "S23 Ultra"
    assert product_Smartphone1.memory == 256
    assert product_Smartphone1.color == "Серый"


def test_Smartphone_add(product_Smartphone1, product_Smartphone2):
    assert product_Smartphone1 + product_Smartphone2 == 2580000.0


def test_Smartphone_add_error(product_Smartphone1):
    with pytest.raises(TypeError):
        result = product_Smartphone1 + 1
