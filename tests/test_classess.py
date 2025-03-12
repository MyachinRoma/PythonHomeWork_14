from src.classess import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.products_in_list) == 3
    
def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.list_product) == 3


    assert first_category.category_count == 2
    assert second_category.product_count == 4



def test_category_products_property(first_category):
    assert (first_category.products == '\nSamsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                       'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')




def test_product(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_new_product():
    product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    product.name = "55\" QLED 4K"
    product.description = "Фоновая подсветка"
    product.price = 123000.0
    product.quantity = 7

def test_price_update(capsys, product):
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'
