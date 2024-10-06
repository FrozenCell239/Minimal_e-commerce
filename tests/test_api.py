import unittest
from app import create_app
from app.models.product import Product
from flask_unittest import ClientTestCase
from json import loads


class OKTest(ClientTestCase):
    app = create_app()

    def setUp(self, client) -> None : self.client = client
    def tearDown(self, client) -> None : pass

    def testIndex(self, client) -> None :
        """
        First rest the index route to ensure that the API works.
        """

        response = client.get('/api/')
        self.assertEqual(response.status_code, 200)
        data = loads(response.data)
        self.assertEqual(data, {'message' : "Hello world !"})

    def testProductList(self, client) -> None :
        """
        Test the product list route to ensure that it works.
        """

        response = client.get('/api/product/list')
        self.assertEqual(response.status_code, 200)
    
    def testProductCreate(self, client) -> None :
        """
        Test the product create route to ensure that it works.
        """

        response = client.post('/api/product/create', json = {
            'name' : "Test product",
            'price' : 18.99,
            'description' : "This is a test product. You don't need to buy it.",
            'stock' : 324
        })
        self.assertEqual(response.status_code, 200)
        data = loads(response.data)
        self.assertEqual(data, {'message' : "Product created successfully !"})

    def testProductUpdate(self, client) -> None :
        """
        Test the product update route to ensure that it works.
        """
        
        with self.app.app_context() :
            product = Product.query.filter_by(name = "Test product").first()
            response = client.put('/api/product/update', json = {
                'id' : product.id,
                'name' : "Test product MODIFIED",
                'price' : 918.99,
                'description' : "This is a modified test product. You still don't need to buy it.",
                'stock' : 24
            })
        self.assertEqual(response.status_code, 200)
        data = loads(response.data)
        self.assertEqual(data['message'], "Product updated successfully !")

    def testProductDelete(self, client) -> None :
        """
        Test the product delete route to ensure that it works.
        """

        with self.app.app_context() :
            product = Product.query.filter_by(name = "Test product MODIFIED").first()
            response = client.delete('/api/product/delete', json = {'id' : product.id})
        self.assertEqual(response.status_code, 200)
        data = loads(response.data)
        self.assertEqual(data['message'], "Product deleted successfully !")

class KOTest(ClientTestCase):
    app = create_app()

    def setUp(self, client) -> None : self.client = client
    def tearDown(self, client) -> None : pass

    # Testing first if API is working
    def testIndex(self, client) -> None :
        """
        First rest the index route to ensure that it works.
        """

        response = client.get('/api/')
        self.assertEqual(response.status_code, 200)
        data = loads(response.data)
        self.assertNotEqual(data, {'message' : "Good bye world !"})
    
    def  testProductCreateWrong(self, client) -> None :
        """
        Tests if the product create fails succeessfully when the product already exists or get a wrong parameter.
        """

        # Testing if the product already exists
        response = client.post('/api/product/create', json = {
            'name' : "Test product",
            'price' : 18.99,
            'description' : "This is a test product. You don't need to buy it.",
            'stock' : 324
        })
        response = client.post('/api/product/create', json = {
            'name' : "Test product",
            'price' : 18.99,
            'description' : "This is a test product. You don't need to buy it.",
            'stock' : 324
        })
        self.assertEqual(response.status_code, 400)
if __name__ == '__main__' : unittest.main()