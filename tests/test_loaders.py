from django.test import TestCase
from src.linein.registry import register, load_data, load_all_data
from src.linein.source import *
from .models import *
from .loaders import *

CATEGORY = 'sample'
USER_COUNT = 3
TAG_COUNT = 4
PRODUCT_COUNT = 2
ORDER_COUNT = 2


class TestLoaders(TestCase):
    def setUp(self):
        register(UserLoader, category=CATEGORY, source=JSONFileSource('tests/samples/users.json'))
        register(TagLoader, category=CATEGORY, source=JSONFileSource('tests/samples/tags.json'))
        register(ProductLoader, category=CATEGORY, source=MIXONFolderSource('tests/samples/products'))
        register(OrderLoader, category=CATEGORY, source=JSONFileSource('tests/samples/orders.json'))

    def test_load_users(self):
        load_data(User, category=CATEGORY)
        self.assertEqual(User.objects.count(), USER_COUNT)
        carol = User.objects.get(username='carol')
        self.assertEqual(carol.name, 'Carol')

    # tests deps, m2m
    def test_load_products(self):
        load_data(Product, category=CATEGORY, with_deps=True)
        self.assertEqual(Tag.objects.count(), TAG_COUNT)
        self.assertEqual(Product.objects.count(), PRODUCT_COUNT)
        watch = Product.objects.get(id='watch')
        self.assertTrue(watch.tags.count(), 2)
        sport_tag = Tag.objects.get(name='sport')
        self.assertIn(sport_tag, watch.tags.all())

    # tests deps, fk, m2m with through
    def test_load_orders(self):
        self._test_orders()

    def test_load_orders_alt_method(self):
        register(AltOrderLoader, category=CATEGORY, source=JSONFileSource('tests/samples/orders.json'))
        self._test_orders()
        print(OrderProductEntry.objects.all())

    def _test_orders(self):
        load_data(Order, category=CATEGORY, with_deps=True)
        self.assertEqual(User.objects.count(), USER_COUNT)
        self.assertEqual(Order.objects.count(), ORDER_COUNT)
        order1 = Order.objects.get(id='o001')
        self.assertEqual(order1.user.name, 'Alice')
        self.assertEqual(order1.products.count(), 1)

    def test_load_all_data(self):
        print("Loading All Data")
        load_all_data(category=CATEGORY)
        self.assertEqual(User.objects.count(), USER_COUNT)
        self.assertEqual(Order.objects.count(), ORDER_COUNT)
        self.assertEqual(Tag.objects.count(), TAG_COUNT)
        self.assertEqual(Product.objects.count(), PRODUCT_COUNT)
        print("End Loading")