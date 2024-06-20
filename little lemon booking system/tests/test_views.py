from django.test import TestCase, Client
from restaurant.models import Menu
from django.contrib.auth.models import User


# https://docs.djangoproject.com/en/5.0/topics/testing/overview/
# https://docs.djangoproject.com/en/5.0/topics/testing/tools/
class MenuViewTest(TestCase):
    def setUp(self):
        self.menuItem1 = Menu.objects.create(id=1, title="scrambledEggs", price=15, inventory=10)
        self.menuItem2 = Menu.objects.create(id=2, title="boiledEggs", price=5, inventory=20)
        self.menuItem3 = Menu.objects.create(id=3, title="Potatoes!", price=3, inventory=15)
        self.menuItem4 = Menu.objects.create(id=4, title="Carbonara", price=12, inventory=30)

    def test_getall(self):
        user = User.objects.create_user(username='testuser', password='test1234!')
        client = Client()
        client.force_login(user)
        response = client.get("http://127.0.0.1:8000/restaurant/menu/")
        serialized_menus = 200
        self.assertEqual(response.status_code, serialized_menus)