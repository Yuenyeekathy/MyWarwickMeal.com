# The draft of the code in this whole file was generated by AI and I modified it according to the actual situation

import unittest
from flask import Flask
from app import app, cart, calculate_total_price

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize the test environment before each test method
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        # Clean up the test environment after each test method
        pass

    def test_index_route(self):
        # Test if the index route returns 200 OK
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        # Test the functionality of adding items to the cart
        with app.test_request_context():
            cart.clear()
            response = self.app.post('/add_to_cart', data={'item_name': 'TestItem', 'item_quantity': 3, 'item_price': 10.0})
            self.assertEqual(response.status_code, 302)  # 302 indicates a redirect
            self.assertEqual(cart['TestItem']['quantity'], 3)

    def test_delete_items(self):
        # Test the functionality of deleting items from the cart
        with app.test_request_context():
            cart.clear()
            cart['TestItem'] = {'quantity': 5, 'price': 8.0}
            response = self.app.post('/delete_items', data={'selected_items': ['TestItem']})
            self.assertEqual(response.status_code, 302)  # 302 indicates a redirect
            self.assertNotIn('TestItem', cart)

    def test_view_cart_route(self):
        # Test if the view cart route returns 200 OK
        response = self.app.get('/cart')
        self.assertEqual(response.status_code, 200)

    def test_calculate_total_price(self):
        # Test the functionality of calculating the total price of items in the cart
        test_cart = {'Item1': {'quantity': 2, 'price': 5.0}, 'Item2': {'quantity': 3, 'price': 8.0}}
        total_price = calculate_total_price(test_cart)
        self.assertEqual(total_price, '34.00')

    def test_login_route(self):
        # Test if the login route returns 200 OK
        response = self.app.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_route(self):
        # Test if the register route returns 200 OK
        response = self.app.get('/login/register/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
