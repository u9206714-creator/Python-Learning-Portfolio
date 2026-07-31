import unittest
from shopping_list import ShoppingList  #from 文件名 import 函数名/类名

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({'tissue':8,'hat':30,'slipper':15})

    def test_get_item_count(self):
        self.assertAlmostEqual(self.shopping_list.get_item_count(),3)

    def test_get_total_price(self):
        self.assertAlmostEqual(self.shopping_list.get_total_price(),53)












