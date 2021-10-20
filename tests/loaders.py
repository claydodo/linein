from src.linein.loader import Loader
from tests.models import *
from tests.serializers import *


class UserLoader(Loader):
    model = User
    serializer_class = UserSerializer


class TagLoader(Loader):
    model = Tag
    serializer_class = TagSerializer


class ProductLoader(Loader):
    model = Product
    serializer_class = ProductSerializer


class OrderLoader(Loader):
    model = Order
    serializer_class = OrderSerializer
