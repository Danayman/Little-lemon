from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=1, title="scrambledEggs", price=15, inventory=10)
        self.assertEqual(item.title, "scrambledEggs")
        self.assertEqual(item.price, 15)
#        self.assertEqual(item.inventory, 10)