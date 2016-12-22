import pytest


def test_cart(app):
    app.add_products_to_cart(number_of_products=3)
    app.remove_products_from_cart()
