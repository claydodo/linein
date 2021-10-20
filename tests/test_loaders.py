from django.test import TestCase
from src.linein.registry import register, load_data
from src.linein.source import *
from .models import *
from .loaders import *

CATEGORY = 'sample'
USER_COUNT = 3
ORDER_COUNT = 2


class TestLoaders(TestCase):
    @classmethod
    def setUpClass(cls):
        register(UserLoader, category=CATEGORY, source=JSONFileSource('tests/samples/users.json'))
        register(OrderLoader, category=CATEGORY, source=JSONFileSource('tests/samples/orders.json'))

    @classmethod
    def tearDownClass(cls):
        pass

    def test_load_users(self):
        load_data(User, category=CATEGORY)
        self.assertEqual(User.objects.count(), USER_COUNT)
        carol = User.objects.get(username='carol')
        self.assertEqual(carol.name, 'Carol')

    # tests deps, fk
    def test_load_orders(self):
        load_data(Order, category=CATEGORY, with_deps=True)
        self.assertEqual(User.objects.count(), USER_COUNT)
        self.assertEqual(Order.objects.count(), ORDER_COUNT)
        order1 = Order.objects.get(id='o001')
        self.assertEqual(order1.user.name, 'Alice')
