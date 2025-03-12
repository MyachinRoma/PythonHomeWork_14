import pytest
from src.classess import Product, Category


@pytest.fixture
def product_apple():
    return Product("Apple", "red", 99.9, 1000)


def test_init_product(product_apple):
    assert product_apple.name == "Apple"
    assert product_apple.description == "red"
    assert product_apple.price == 99.9
    assert product_apple.quantity == 1000


@pytest.fixture
def category_fruit():
    return Category("fruits", "fruits from India", ["banana", "mango"])


def test_init_category(category_fruit):
    assert category_fruit.name == "fruits"
    assert category_fruit.description == "fruits from India"
    assert category_fruit.products == ["banana", "mango"]
    assert category_fruit.product_count == 2
    assert Category.category_count == 1
