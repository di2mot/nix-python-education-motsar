from to_test import *
from freezegun import freeze_time
import pytest


@pytest.mark.parametrize("test_input, expected", [(6, "even"), (7, "odd")])
def test_even_odd(test_input, expected):
    """result of check. `even` if given number is even
            and `odd` if the number is odd."""
    assert even_odd(test_input) == expected


def test_sum_all():
    """nt or float: the result of adding all numbers together."""
    assert sum_all(1, 2, 3) == 6, 'Expected 6'
    assert sum_all(-1, -2, -3) == -6, 'Expected -6'
    assert sum_all(1.0, 2.0, 3.0) == 6.0, 'Expected 6.0'
    assert sum_all(1, 2, 3.0) == 6.0, 'Expected 6.0'
    assert sum_all(3, 2, 1) == 6, 'Expected 6'


@freeze_time("4:20")
def test_time_night():
    """ current time of day. Could be: "night" """
    assert time_of_day() == "night"


@freeze_time("8:30")
def test_time_morning():
    """ current time of day. Could be: "morning" """
    assert time_of_day() == "morning"


@freeze_time("17:30")
def test_time_afternoon():
    """ current time of day. Could be: "morning"afternoon" """
    assert time_of_day() == "afternoon"


@pytest.fixture()
def some_product(title='Newproduct', price=3.50, quantity=10):
    """ Create fixture for testing """
    return Product(title, price, quantity)


@pytest.mark.parametrize("test_input, expected", ([9, 1], [7, 3]))
def test_product_quantity(some_product, test_input, expected):
    """ Reducing the quantity of item """
    some_product.subtract_quantity(test_input)
    assert some_product.quantity == expected, "The quantity of products should not be negative"


@pytest.mark.parametrize("test_input, expected", ([2, 12], [1, 11]))
def test_product_add_quantity(some_product, test_input, expected):
    """ Add quantity of item """
    some_product.add_quantity(test_input)
    assert some_product.quantity == expected, "the number of products increased"


@pytest.mark.parametrize("test_input, expected", ([6, 6], [10, 10]))
def test_product_price(some_product, test_input, expected):
    """ Change price of products """
    some_product.change_price(test_input)
    assert some_product.price == expected, "The price must be equal to the new price"


@pytest.fixture()
def some_shop():
    """ Create fixture for testing """
    return Shop(Product(title='nVidia RTX 3080Ti', price=3_500, quantity=1))


@pytest.mark.parametrize("test_input, expected", (
        [Product(title='Nokia', price=35.0, quantity=10), 'Nokia'],
        [Product(title='Schmetterling', price=3.50, quantity=100_000), 'Schmetterling']))
def test_product_price(some_shop, test_input, expected):
    """ Testing add products"""
    some_shop.add_product(test_input)
    assert some_shop.products[1].title == expected, "Product not added"


@pytest.mark.parametrize("test_input, expected", (['nVidia RTX 3080Ti', 5],
                                                  ['Schmetterling', 1]))
def test_product_price(some_shop, test_input, expected):
    """ Testing selling of products"""
    some_shop.add_product(Product(title='nVidia RTX 3080Ti', price=3_500, quantity=5))
    some_shop.sell_product(product_title=test_input)
    assert some_shop.products[0].quantity == expected, "Wrong amount of money"
