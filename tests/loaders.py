from src.linein.loader import Loader
from tests.models import *
from tests.serializers import *


class UserLoader(Loader):
    model = User
    serializer_class = UserSerializer


class OrderLoader(Loader):
    model = Order
    serializer_class = OrderSerializer
