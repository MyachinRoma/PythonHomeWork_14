class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, dict_product):
        return cls(dict_product['name'], dict_product['description'], dict_product['price'], dict_product['quantity'])

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        self.__price = new_price


class Category:
    name: str
    description: str
    list_product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__list_product = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f'{self.name}, колличество продуктов: {Category.product_count} шт.'

    def add_product(self, product: Product):
        self.__list_product.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ''
        for product in self.__list_product:
            product_str += f'\n{str(product)}'
        return product_str

    @property
    def products_in_list(self):
        return self.__list_product
