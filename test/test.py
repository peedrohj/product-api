import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"
BASE_PRODUCTS_URL = f'{BASE_URL}/product'


class ApiTest(unittest.TestCase):
    """
        Some unit tests for the Api
    """

    # Create a product test example
    PROCUT_OBJ = {
        "name": "Teste",
        "description": "A product created for test the Api"
    }

    # GET request to /product/get_all returns all products

    def test_get_all_products(self):
        request = requests.get(f'{BASE_PRODUCTS_URL}/get_all')
        request_obj = request.json()

        self.assertEqual(request.status_code, 200)
        self.assertEqual(list(request_obj.keys()), ['data', 'status'])

    # POST request to /product/cereate returns a message with the was created wiht success
    def test_create_product(self):
        request = requests.post(
            f'{BASE_PRODUCTS_URL}/create',
            params={'name': self.PROCUT_OBJ["name"],
                    'description': self.PROCUT_OBJ["description"]},

        )

        request_obj = request.json()
        self.PROCUT_OBJ['id'] = request_obj['data']['id']

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request_obj['data']['name'], self.PROCUT_OBJ['name'])

    # GET request to /product/get/<id> returns one product
    def test_get_one_product(self):
        product_id = self.PROCUT_OBJ["id"]
        request = requests.get(
            f'{BASE_PRODUCTS_URL}/get/{product_id}')
        request_obj = request.json()

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request_obj['data']['name'], self.PROCUT_OBJ['name'])

    # GET request to /product/get/<id> returns one product
    def teste_delete_one_product(self):
        product_id = self.PROCUT_OBJ["id"]
        request = requests.delete(
            f'{BASE_PRODUCTS_URL}/delete/{product_id}')
        request_obj = request.json()

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request_obj['status'], 'success')


if __name__ == "__main__":
    unittest.main()
