import pytest


def test_Lawngrass(product_Lawngrass1):
    assert product_Lawngrass1.name == "Газонная трава"
    assert product_Lawngrass1.description == "Элитная трава для газона"
    assert product_Lawngrass1.price == 500.0
    assert product_Lawngrass1.quantity == 20
    assert product_Lawngrass1.country == "Россия"
    assert product_Lawngrass1.germination_period == "7 дней"
    assert product_Lawngrass1.color == "Зеленый"


def test_Lawngrass_test_add(product_Lawngrass1, product_Lawngrass2):
    assert product_Lawngrass1 + product_Lawngrass2 == 16750.0


def test_lawngrass_test_add_error(product_lawngrass1):
    with pytest.raises(TypeError):
        result = product_lawngrass1 + 1
        