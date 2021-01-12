from django.test import TestCase
from rest_framework.test import APIClient
import json

from .models import Stock

# Create your tests here.


class StockDetailTestCase(TestCase):
    def setUp(self):
        self.cheese = Stock(name="Cheese", quantity=10, price=5.0)
        self.cheese.save()
        self.client = APIClient()

    def test_create_stock(self):
        data = {
            "name": "Banana",
            "price": 1,
            "quantity": 100
        }
        resp = self.client.post('/stock/', data=data)
        self.assertEqual(resp.json().get("name"), "Banana")

    def test_get_cheese_by_sku(self):
        cheese = self.client.get('/stock/{}/'.format(self.cheese.sku))
        cheese = cheese.json()
        self.assertEqual(cheese.get("sku"), str(self.cheese.sku))

    def test_update_cheese_quantity(self):
        cheese = self.client.get(
            '/stock/{}/{}/'.format(self.cheese.sku, 1)
        )
        cheese = cheese.json()
        self.assertEqual(cheese.get("quantity"), 11)

    def test_reduce_cheese_quantity(self):
        cheese = self.client.get(
            '/stock/{}/{}/'.format(self.cheese.sku, -1)
        )
        # print(cheese)
        cheese = cheese.json()
        self.assertEqual(cheese.get("quantity"), 9)


class StockListTestCase(TestCase):
    def setUp(self):
        self.cheese = Stock(name="Cheese", quantity=10, price=5.0)
        self.cheese.save()
        self.bacon = Stock(name="Bacon", quantity=5, price=25.0)
        self.bacon.save()
        self.toliet_paper = Stock(name="Toliet paper", quantity=0, price=2.0)
        self.toliet_paper.save()
        self.toliet_paper = Stock(name="Newpaper", quantity=1, price=1.50)
        self.toliet_paper.save()

        self.client = APIClient()

    def test_query_quantity(self):
        resp = self.client.get("/stock/?quantity=0")
        results = resp.json()
        self.assertEqual(len(results), 1)
        self.assertEquals(float(results[0].get("price")), 2.0)

    # def test_query_quantity_in_stock_failure(self):
    #     resp = self.client.get("/stock/?in_stock=True")
    #     results = resp.json()
    #     self.assertEqual(len(results), 3)
    #
    # Left it out, but# I'd like to make
    # a dereived value for ease of use.

    def test_query_quantity_in_stock(self):
        resp = self.client.get("/stock/?min_quantity=1")
        results = resp.json()
        self.assertEqual(len(results), 3)
